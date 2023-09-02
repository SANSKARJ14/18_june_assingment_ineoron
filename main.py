#18 june assingment

"""
1. What is the role of the 'else' block in a try-except statement? Provide an example
scenario where it would be useful.

The 'else' block in a try-except statement is optional and serves as a code block that will execute only
if no exceptions are raised within the 'try' block.

example

def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    else:
        print(f"The result of {num1} divided by {num2} is: {result}")

"""
"""
2. Can a try-except block be nested inside another try-except block? Explain with an
example.

yes try-except block be nested inside another try-except block.

example

def square_of_reciprocal(numbers):
    square_results = []
    for num in numbers:
        try:
            reciprocal = 1/num
        except ZeroDivisionError:
            print("error: you cannot divide by zero ")
            square_results.append(None)
        except TypeError:
            print ("error: invalid input")
            square_results.append(None)
        else:
            try:
                square_result = reciprocal ** 2
            except TypeError:
                print("error: invalid input for square calulation")
            else:
                square_results.append(square_result)
    return square_results


number_list = [2,3,'a',0,72]
results = square_of_reciprocal(number_list)
print(results)

"""
"""
3. How can you create a custom exception class in Python? Provide an example that
demonstrates its usage.


class invalid_input_error(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

def square_root_calculation(number):
    if number < 0:
        raise invalid_input_error("number must be positive")
    return number ** .5

try:
    num = float(input("Enter a positive number: "))
    result = square_root_calculation(num)
    print("Square root of", num, "is:", result)
except invalid_input_error as e :
    print("error :",str(e)  )
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

"""
"""
4. What are some common exceptions that are built-in to Python?

SyntaxError: Raised when there is a syntax error in the code, indicating that the code is not properly
written or formatted.

IndentationError: Raised when there is an issue with the indentation of the code,
such as mismatched indentation levels.

NameError: Raised when a name or variable is not found in the current scope or namespace.

TypeError: Raised when an operation or function is applied to an object of an inappropriate data type.

ValueError: Raised when a function or operation receives an argument of the correct data type but 
with an inappropriate value.

ZeroDivisionError: Raised when attempting to divide by zero.

IndexError: Raised when trying to access an index of a sequence (e.g., list, tuple) that is out of range.

KeyError: Raised when trying to access a key that does not exist in a dictionary.

AttributeError: Raised when an attribute or method is not found on an object.

FileNotFoundError: Raised when trying to access a file that does not exist.

ImportError: Raised when there is an issue with importing a module or package.

MemoryError: Raised when the program runs out of available memory.

OverflowError: Raised when a mathematical operation exceeds the maximum representable value.

IOError: Raised when there is an input/output error, such as when reading or writing to a file.
"""
"""
5. What is logging in Python, and why is it important in software development?

Logging in Python refers to the process of recording and storing important information, status,
or events that occur during the execution of a program.

Logging is a vital aspect of software development with numerous benefits.
It helps developers troubleshoot and debug applications by providing valuable insights into the program's
 behavior when errors occur. In production environments, logging allows monitoring performance and 
detecting anomalies, helping to identify bottlenecks and ensure the apllication
health Additionally, logging plays a critical role in auditing and compliance, recording user actions and
critical events. It enables prompt error reporting to developers or system administrators,
facilitating timely issue resolution.
By saving logs over time, historical analysis unveils trends and long-term behavior, aiding in optimization.
The logging module flexibility allows granular control over log levels,
enabling the activation of detailed logging as needed.

"""
"""

6. Explain the purpose of log levels in Python logging and provide examples of when
each log level would be appropriate.

The purpose of log levels in Python logging is to categorize log messages based on their severity or importance.
Log levels allow developers to control the verbosity of logging and filter out messages based on their significance.

The common log levels, in increasing order of severity, are:

a)dubug

Detailed information, useful for debugging and understanding the flow of the program.
It's typically used during development and should be disabled in production environments to avoid excessive logging.

b)INFO: 

General information about the application's execution. It's used to provide useful status updates
and is generally safe for production environments.

c)WARNING:

Indicates a potential issue or an unexpected situation that may not be an error but needs attention.
It's used to alert about possible problems.

d)ERROR: 

Indicates a specific error that occurred during the execution of the application. 
It's used to report errors that need investigation and correction.

e)CRITICAL:

Indicates a severe error or a critical situation that may lead to the termination of the application.
It's used for very severe problems that require immediate attention

"""

"""
7). What are log formatters in Python logging, and how can you customise the log
message format using formatters?

log formatters are used to define the format of log messages when they are emitted by the logging system.
Log messages typically contain information about the event being logged, such as the log level, timestamp,
the name of the logger, and the actual log message.
Formatters allow you to customize how this information is presented in the log messages.

how to customize.

To customize the log message format in Python using formatters, you can follow these steps.
First, import the logging module.
Then, create a logger with a unique name. Next, define a formatter by creating an instance of logging.Formatter
and specifying a format string with placeholders for elements like timestamp, log level, logger name, and log message.
Afterward, create a handler (e.g., StreamHandler for console output) and associate the formatter with it using handler.
setFormatter(formatter). Add the handler to your logger with logger.addHandler(handler).
Now, you can use the logger to log messages, and the formatter will format them as per your format string.
To further customize the format, adjust the format string by including or excluding placeholders and adding static text.
This way, you can tailor the log message format to your specific needs, ensuring the right level of detail and context
in your log messages.


"""
"""

8. How can you set up logging to capture log messages from multiple modules or
classes in a Python application?

to set up logging for capturing log messages from multiple modules or classes in Python application,follow these steps.
First, import the logging module. Next, create a separate logger for each module or
class using logging.getLogger(__name__). This associates each logger with its respective module or class.

In your main script or application entry point, configure the logging system. Specify log handlers
(e.g., StreamHandler for console output), set log levels, and define a common log format.
Add these handlers to the root logger with the desired settings.

Within each module or class, utilize the logger created earlier to log messages at various log levels.
This separation ensures that log messages are directed to the appropriate handlers and adhere to the defined log format.

When you run your Python application, the central logging system will capture and manage log messages from
different modules or classes, providing consistency in formatting and global logging settings while allowing for
flexibility in individual modules or classes.
"""

"""

9. What is the difference between the logging and print statements in Python? When
should you use logging over print statements in a real-world application? 

The key difference between logging and print statements in Python is that logging is a structured and customizable way
to record information, whereas print statements are primarily for debugging and displaying information
during development.

Use logging over print statements in a real-world application when you need to:

A.)Traceability: Logging provides a record of events and can include timestamps, log levels, and loggers' names,
making it easier to trace and diagnose issues in a production environment.

B.)Configurability: Logging allows you to configure where log messages go (e.g., console, files, databases)
and set different log levels, so you can control what information is recorded without modifying code.

C.)Security: In production, you may want to suppress sensitive information from being displayed,
which is possible with logging but not with print statements.

D.)Maintenance: Log messages can be left in the code and controlled via configuration, while print statements 
often need to be removed or commented out during code cleanup.

In summary, use logging for structured and controlled information recording in real-world applications,
especially when traceability, configurability, and security are important.
Use print statements for temporary debugging during development.
"""
"""

10. Write a Python program that logs a message to a file named "app.log" with the
following requirements:
● The log message should be "Hello, World!"
● The log level should be set to "INFO."
● The log file should append new log entries without overwriting previous ones.


import logging

logging.basicConfig(
    filename='app.log',  # Log file name
    level=logging.INFO,  # Log level set to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',
)

# Log the message
logging.info('Hello, World!')

"""
"""
11. Create a Python program that logs an error message to the console and a file named
"errors.log" if an exception occurs during the program's execution. The error
message should include the exception type and a timestamp.

import logging
import sys
import traceback

# Configure the logger
logging.basicConfig(
    level=logging.ERROR,  # Log level set to ERROR to capture exceptions
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('errors.log'),  # Log errors to a file
        logging.StreamHandler(sys.stderr),  # Log errors to the console
    ]
)

try:
    # Your code that may raise an exception goes here
    result = 10 / 0  # Example: Division by zero to trigger an exception
except Exception as e:
    # Log the exception details
    logging.error(f'Exception: {str(e)}')
    logging.error(traceback.format_exc())

"""