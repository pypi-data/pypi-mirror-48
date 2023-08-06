# Noisemap
 A simple library for python which returns a noisemap as a 2D numpy array.

## Installation

` pip install noisemap `

## Usage

### Functions

#### Mapgen

` Mapgen(size, smoothness) `

##### Parameters

###### `size`

`size` defines how many data points are in the array. The noisemaps generated are always square, so a map with `size` 5 would be a 5x5 2D array.

###### `smoothness`

`smoothness` affects how smoothed out the noisemap is. A `smoothness` of 0 would be a grid of completely random numbers, whereas a higher `smoothness` would have each data point be relatively close in value to its adjacent data points.

##### Notes

* All datapoints are floating point numbers generated with `random.random()`. This means you can affect the numbers in the noisemap with `random.seed(seed)`.
* Smoothing can take some time depending on the size of the grid and the amount of smoothing to be done.