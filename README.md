# min-driving_NY_Parks
Using Google maps API to calculate which New York State Park(103 of them) can be driving for reasonable times.

The use of travelling time is deprecated by Google Maps' term of use but I do not plan to use this in any commercial way. I'm just doing this for programming practise. 

Right now google limit python request to 10(I need 103*102/2 = 5253...way over 10) and I need to find a way to bypass it since the ultimate goal is to make the park a weighted undirected graph so that I can find the shortest path to get to them all

New York State Parks: https://parks.ny.gov/recreation/trails/trails-in-state-parks.aspx
Google Map Pytho API: https://github.com/googlemaps/google-maps-services-python
Possible Python Graph solution: http://networkx.github.io