#!/bin/bash

echo "Activating virtual environment..."
source venv/bin/activate

echo "Running tests with pytest..."
pytest tests/ --verbose --disable-warnings

if [ $? -eq 0 ]; then
    echo "All tests passed successfully."
else
    echo "Some tests failed. Please check the output above for details."
    exit 1
fi

echo "Tests completed."
