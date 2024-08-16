import time


def perform_task():
    print("Task started.")
    # Simulate a task that takes some time
    time.sleep(1.5)
    print("Task completed.")


def log_time_and_perform_task():
    start_time = time.time()
    for i in range(3):
        # Log the current time
        current_local_time = time.localtime()
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_local_time)
        print(f"Log {i+1}: Current Time: {formatted_time}")

        # Perform the task
        perform_task()

        # Pause for a while before the next iteration
        time.sleep(2)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Total Elapsed Time: {elapsed_time:.2f} seconds")


log_time_and_perform_task()
