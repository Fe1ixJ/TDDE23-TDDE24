from lab5b import *

def test_constraint():
    '''Test constraint.'''
    function = pixel_constraint(100, 150, 50, 200, 100, 255)
    try:
        # Test cases with valid and invalid values
        assert function((100, 100, 100)) == 1 
        assert function((99, 100, 255)) == 0
        assert function((101, 201, 255)) == 0

        # Value range test
        try:
            assert function((100, 100, 256)) == 0
            assert function((100, -100, 100)) == 0
        except ValueError as error:
            pass
        else:
            raise AssertionError("Expected ValueError")

        # Value Error test
        try:
            function((100, 100, 100, 100))
        except ValueError:
            pass
        else:
            raise AssertionError("Expected ValueError")

        # Type Error test
        try:
            function((100, 100, "100"))
            function((100, 100, [100]))
            function((100, 100, (100,)))
            function((100, 100, None))
        except TypeError:
            pass
        else:
            raise AssertionError("Expected TypeError")
        

    except AssertionError as error:
        print(f"Test failed, AssertionError: {error}")
    except TypeError as error:
        print(f"Test failed, AssertionError: {error}")
    except ValueError as error:
        print(f"Test failed, AssertionError: {error}")
    else:
        print("Test passed")


def test_generator_from_image(): 
    '''Test generator_from_image.'''
    test_list = [(1,2,3), (4, 'a', 6), (7, 8, 9.0)]
    index = generator_from_image(test_list)
    try:
        # Test cases with valid values
        try:
            assert index(0) == (1, 2, 3)
            assert index(1) == (4, 'a', 6)
            assert index(2) == (7, 8, 9.0)
        except ValueError as error:
            raise AssertionError("Expected ValueError as input is not a list of correct tuples")
        # Test cases with invalid values
        try:
            assert index(0) == (0, 2, 3)
            assert index(1) == (4, 'A', 6)
            assert index(2) == (7, 8, 9)
            assert index(0) == (1, 10, 3)
            assert index(1) == (4, 'a', 6)
            assert index(2) == (7, 9, 8.0)
        except AssertionError as error:
            pass
        else:
            raise AssertionError("Expected IndexError at wrong input")

        # Test cases with invalid index
        try:
            wrong = index(len(test_list))
            print(f"Success for {test_list[len(test_list)]}: result {wrong}")
        except IndexError as error:
            pass
        else:
            raise AssertionError("Expected IndexError at index out of range") 

        # Test cases with invalid input
        try:
            wrong = generator_from_image(test_list[len(test_list)+1])
            print(f"success for {test_list[len(test_list)+1]}: result {wrong}")
        except IndexError as error:
            pass
        else: 
            raise AssertionError("Expected IndexError for the input out of range exception")


    except AssertionError as error:
        print(f"Test failed, AssertionError: {error}")
    except IndexError as error:
        print(f"Test failed, IndexError: {error}")
    except TypeError as error:
        print(f"Test failed, TypeError: {error}")
    else:
        print("Test passed")

def test_combine_images():
    '''Test combine_images.'''
    condition = pixel_constraint(100,150,50,200,100,255)
    hsv1 = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
    hsv2 = [(100, 100, 100), (100, 100, 100), (100, 100, 100),(100, 100, 100)]
    hsv3 = [(256,100,100),(100,-100,0), (100,100,100)] 
    
    generator1 = generator_from_image([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    generator2 = generator_from_image([(10, 11, 12), (13, 14, 15), (16, 17, 18),])
    generator3 = generator_from_image([(1,1),(2,2)])
    generator4 = generator_from_image([(3,3,4),(4,4,4)])
    generator5 = generator_from_image([(1,1,1),(2,2,2),(3,3,3)])
    generator6 = generator_from_image([(4,4,4),(5,5,5)])

    try:
        # Test cases with valid values
        try:
            result = combine_images(hsv1, condition, generator1, generator2)
            for i in range(len(result)):
                assert len(result[i]) == len(hsv1[i]), f"Expected length of {len(hsv1[i])}, but got {len(result[i])}"
        except IndexError:
            raise AssertionError("Expected IndexError")

        # Test cases with invalid values
        try:
            result = combine_images(hsv1, condition, generator3, generator4)
            for i in range(len(result)):
                assert len(result[i]) == len(hsv1[i]), f"Expected length of {len(hsv1[i])}, but got {len(result[i])}"
        except IndexError:
            pass
        else: 
            raise AssertionError("Expected IndexError")

        # Test cases with invalid values
        try:
            combine_images(hsv1, condition, generator5, generator6)
        except IndexError as error:
            pass
        else:
            raise AssertionError("Expected IndexError")
        
        # Test cases with invalid values
        try:
            result = combine_images(hsv2, condition, generator1, generator2)
            for i in range(len(result)):
                assert len(result[i]) == len(hsv2[i]), f"Expected length of {len(hsv2[i])}, but got {len(result[i])}"
        except IndexError as error:
            pass
        else:
            raise AssertionError("Expected IndexError")
        
        # Test cases with invalid values
        try:
            result = combine_images(hsv3, condition, generator1, generator2)
            for i, (h, s, v) in enumerate(hsv3):
                assert 0 <= h < 256 and 0 <= s < 256 and 0 <= v < 256, f"Expected values between 0 and 255, but got {h}, {s}, {v}"
        except ValueError as error:
            pass
        except IndexError as error:
            pass
        else:
            raise AssertionError("Expected AssertionError")

    except AssertionError as error:
        print(f"Test failed, AssertionError: {error}")
    except IndexError as error:
        print(f"Test failed, IndexError: {error}")
    except TypeError as error:
        print(f"Test failed, TypeError: {error}")
    else:
        print("Test passed")

if __name__ == "__main__":
    test_constraint()
    test_generator_from_image()
    test_combine_images()
