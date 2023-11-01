import Enum
import SumNumbersInRange
import DefRunTime

if __name__ == '__main__':
 #   Enum.program_to_calculate_area()
    print(DefRunTime.calculate_run_time(SumNumbersInRange.sumNumberInRange, 100000000,4))
    print(DefRunTime.calculate_run_time(SumNumbersInRange.sumNumberInGenerator, 100000000,4))
    print(DefRunTime.calculate_run_time(SumNumbersInRange.sumNumberInLoop, 100000000,4))
    print(DefRunTime.calculate_run_time(SumNumbersInRange.sumNumberByArythmetic, 100000000,4))