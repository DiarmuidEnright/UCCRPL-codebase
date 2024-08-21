if ! command -v py-spy &> /dev/null; then
    echo "py-spy not found. Install it first."
    exit 1
fi

python3 profiler_main.py &
PID=$!

py-spy top --pid $PID

wait $PID
