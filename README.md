# RoadTrip-Optimiser

RoadTrip Optimiser is a web app which allows Users to dynamically select cities( either by clicking on the map or by searching 
through the search text boxes) through which the user wants a Tour and returns the most optimised tour through those cities.
In the backend it solves the symmetric Travelling Salesman Problem using two algorithms

--> Simulated Annealing 
--> Subtour Elimination

It Compares the optimum paths returned from both the algorithms and then selects the one which is the most cost efficient.

Client side scripting has been done in JavaScript and the Server Side scripting has been done in python. The web app is hosted on Django.

Requirements:

1) Install django: sudo apt-get django

2) Install gurobipy: conda install gurobipy (gurobipy requires anaconda to be installed)

3) Obtain a license from the gurobi website and activate it using: grbgetkey


References: 
Googlemaps Api: Customized the standard APIs to fit our use case- https://developers.google.com/maps/documentation/directions/start
Address Autocomplete: Customized the autocomplete API to fit our use case https://jqueryui.com/autocomplete/
CSS template: http://www.w3schools.com/css/ googlemaps API: https://github.com/googlemaps/google-maps-services-python
