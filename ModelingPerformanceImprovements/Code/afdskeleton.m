%% Matlab example code for least squares fitting of AFD model
% Change this to the location where you store the downloaded data
folder = '..\Shared Data\ImprovingPerformance\';
T = readtable( [ folder 'LumositySample_user30222.csv' ] );

g    = T.gameplay;
obsy = T.score;
s    = T.session;
d    = T.dayselapsed;
t    = T.timestamp;

% Show data
figure( 1 ); clf;
subplot(1,2,1);
plot( g , obsy , 'k-o' );
xlabel( 'Gameplay' ); ylabel( 'Score' );
subplot(1,2,2);
plot( t , obsy , 'k-o' );
xlabel( 'Date Gameplay' ); ylabel( 'Score' );

% Create a handle to the function that returns the mean squared
% error for the afd model with parameters p and data s, d , g, and obsy
fun = @(p)afdmodel( p , s , d , obsy );

% Starting parameter values for the optimization procedure (i.e. guesses
% for the parameters that are not too far off from optimal values)
p0(1) = 1;  % parameter c
p0(2) = 30; % parameter u
p0(3) = 10; % parameter b
p0(4) = 5;  % parameter h

% Set the optimizer to "fminunc", the nonlinear optimization procedure without constraints on the parameters
options = optimoptions('fminunc','Display','none');

% Run the optimizer and return the parameters p that minimize the squared deviations
p = fminunc(fun,p0,options);

% Get the predicted scores for best fitting parameters p
[ mse , predy ] = fun( p );

% Report the parameters found
fprintf( 'Best fitting parameters (MSE=%3.3f)\n' , mse );
fprintf( '\tc=%3.3f\n' , p(1) );
fprintf( '\tu=%3.3f\n' , p(2) );
fprintf( '\tb=%3.3f\n' , p(3) );
fprintf( '\th=%3.3f\n' , p(4) );

% Overlay the best fitting curve
subplot(1,2,1); hold on; 
plot(g,predy,'r-');
subplot(1,2,2); hold on;
plot(t,predy,'r-');

function [ mse , predy ] = afdmodel( p , s , d , obsy )
% Function that computes the predicted performance of the afd model given
% parameters c, u , b, and h
c = p( 1 ); % assume that the first parameter is c
u = p( 2 ); % assume that the second parameter is u
b = p( 3 ); % assume that the third parameter is b
h = p( 4 ); % assume that the fourth parameter is h

% ------------------------------------------
% INSERT YOUR CODE HERE TO CALCULATE PREDY
% ------------------------------------------

% Mean squared deviations between predicted and observed scores --
% this is what we want to minimize
mse = nanmean( ( predy - obsy ).^ 2 );

end