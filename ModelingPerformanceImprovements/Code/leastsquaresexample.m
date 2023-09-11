%% Matlab example code for least squares fitting of exponential learning model
% Change this to the location where you store the downloaded data
folder = '..\ImprovingPerformance\'; 
T = readtable( [ folder 'LumositySample_user48567.csv' ] );
t = T.gameplay; % Use gameplay to represent t
obsy = T.score; % Use score to represent y (the observed data)

% Show data
figure( 1 ); clf;
plot( t , obsy , 'k-o' );
xlabel( 'Gameplay' ); ylabel( 'Score' );

% Create a handle to the function that returns the mean squared
% error for the exponential model with parameters p and data t and obsy
fun = @(p)exponentialmodel( p , t , obsy );

% Starting parameter values for the optimization procedure (i.e. guesses
% for the parameters that are not too far off from optimal values)
p0(1) = 0.5; % parameter c
p0(2) = 60;  % parameter a
p0(3) = 40;  % parameter u

% Set the optimizer to "fminunc", the nonlinear optimization procedure without constraints on the parameters 
options = optimoptions('fminunc','Display','iter');

% Run the optimizer and return the parameters p that minimize the squared deviations
p = fminunc(fun,p0,options);

% Get the predicted scores for best fitting parameters p
[ mse , predy ] = fun( p );

% Report the parameters found
fprintf( 'Best fitting parameters\n' );
fprintf( '\tc=%3.3f\n' , p(1) );
fprintf( '\ta=%3.3f\n' , p(2) );
fprintf( '\tu=%3.3f\n' , p(3) );

% Overlay the best fitting curve
hold on; plot(t,predy,'r-');

function [ mse , predy ] = exponentialmodel( p , t , obsy );
% Function that computes the predicted performance of the exponential model at times t given parameters c, a, and u
% Returns the mean squared error (mse) for the predicted and observed
% scores and the model predictions (predy)

c = p( 1 ); % assume that the first parameter is c
a = p( 2 ); % assume that the second parameter is a
u = p( 3 ); % assume that the third parameter is u

% predicted scores
predy = a - ( a - u ) * exp( -c * t );

% Mean squared deviations between predicted and observed scores --
% this is what we want to minimize
mse = nanmean( ( predy - obsy ).^ 2 );
end







