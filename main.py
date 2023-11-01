import Enum
import SumNumbersInRange
import DefRunTime
import checkNumberisInContainer

if __name__ == '__main__':
 #   Enum.program_to_calculate_area()
    print(DefRunTime.calculate_run_time(
        checkNumberisInContainer.is_number_in_collection,
        10000,
        checkNumberisInContainer.listContainer,
        20,
        ))

    print(DefRunTime.calculate_run_time(
        checkNumberisInContainer.is_number_in_collection,
        10000,
        checkNumberisInContainer.setContainer,
        20,
        ))


