CS2300_Program4

part1 Pseudocode===========================================

  Create functions
     # dot product for 2 3x1 column vectors

    # addition for 2 3x1 column vectors

    # subtractions for 2 3x1 column vectors

    # multiplication for 2 3x1 column vectors

    # normalize vector

    # equation: x' = ((q dot n) / (x dot n)) * x //this is perspective
    # perspective projection

    # equation: x' = x + (([q-x] dot n)/(v dot n)) * v //this is parallel
    # parallel projection
    
  Read input file
    # set file name to variable

    # open txt file and copy data

    # organize data into n-dimension array

    # loop to count number of items in matrix
    
    # format matrix
    
  process data
    # count number of rows in input matrix

    # create new matrix with by deleting first row of input matrix

    # parse instructions from first line in matrix

    # normalize n

    # create array of points

    # PROJECTION CALCULATIONS 
    # q = plane point 11, 12, 13
    # n = plane direction 17 18 19
    # x = point x1 x2 x3, x4 x5 x6, x7 x8 x9

    # calculate parallel projections of every point

    # calculate perspective projections of every point

  Data output
    # convert parallel points list to matrix

    # convert perspective points list to matrix

    # write parallel to file

    # write perspective to file

part2 Pseudocode===========================================

  # FUNCTIONS
    # dot product for 2 3x1 column vectors

    # addition for 2 3x1 column vectors

    # subtractions for 2 3x1 column vectors

    # multiplication for 2 3x1 column vectors

    # normalize vector

    # Point normal form of plane

    # find distance using point and plane in point normal form

    # find the cross product of 2 3x1 column vectors

    # calculate the intersection point of a triangle and a line
        # calculate vectors for the line and the triangle edges

        # check if line and triangle are parallel

        # calculate intersection point

  # DATA INPUT
  # set file name to variable

  # open txt file and copy data

  # organize data into n-dimension array
      # loop to count number of items in matrix
      # format matrix

  # INPUT PROCESSING
    # count number of rows in input matrix

    # create new matrix with by deleting first row of input matrix

    # parse instructions from last line in matrix

    # normalize n

    # create point normal form of plane

    # create array of points

    # find distances

  # INPUT PROCESSING part 2
    # count number of rows in input matrix

    # create new matrix with by deleting first row of input matrix

    # parse instructions from first line in matrix

    # find triangles & line intersection

  # DATA OUTPUT 
    # write distances to file

part3 Pseudocode===========================================

  # Function that Computes the dominant eigenvalue and eigenvector of a square matrix using the power method
      # Generate an initial guess for the eigenvector

      # Initialize the eigenvalue and eigenvector

      # Power method iteration

        # Initialize an empty list
        # Initialize a sum variable
        # Add the product of A[i][j] and r[j] to the sum variable
        # Append the sum to the list y

        #check if values are within tolerance
          r = [y[i] / y[j] for i in range(len(y))]
          if abs(lambda_new - lambda_old) < eps:
              return lambda_new, r

      print("maximum iterations exceeded.")
      return None

  # DATA INPUT
    # set file name to variable

    # open txt file and copy data

    # organize data into n-dimension array
        # loop to count number of items in matrix
        # format matrix

    # check for negative values in matrix

    # check that matrix is stochastic

    # use power method to find converging point

  # COMPUTATION
    # set the parameters

    # compute the dominant eigenvalue and eigenvector
        # print the eigenvector indices in descending order of values
        # format indexed so they start at 1 and not 0

  # DATA OUTPUT
    # write eigenvector indices to file





