import win32evtlog
import argparse

# Parse command line arguments with argparse
def parse_args():

    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Read Windows Event Logs and filter by event types.")
    parser.add_argument("--log", type=str, default="Application", help="Specify the log to read (e.g., Application, System, Security)")
    parser.add_argument("--event_types", type=str, nargs='+', default=["error", "warning", "information"],
                        choices=["error", "warning", "information"],
                        help="Event types to filter (choose from 'error', 'warning', 'information').")
    parser.add_argument("--read_mode", type=str, default="forwards",
                        choices=["forwards", "backwards"],
                        help="Specify the read mode for event log (forwards, backwards).")

    # Parse the command-line arguments
    return parser.parse_args()

# Function to get the event type flags based on user input
def get_event_type_flags(event_types):
    flags = 0
    if 'error' in event_types:
        flags |= win32evtlog.EVENTLOG_ERROR_TYPE
    if 'warning' in event_types:
        flags |= win32evtlog.EVENTLOG_WARNING_TYPE
    if 'information' in event_types:
        flags |= win32evtlog.EVENTLOG_INFORMATION_TYPE
    return flags

# Function to return the correct read flag based on the mode
def get_read_flags(read_mode):
    if read_mode == "forwards":
        return win32evtlog.EVENTLOG_SEQUENTIAL_READ | win32evtlog.EVENTLOG_FORWARDS_READ
    elif read_mode == "backwards":
        return win32evtlog.EVENTLOG_SEQUENTIAL_READ | win32evtlog.EVENTLOG_BACKWARDS_READ
    else:
        raise ValueError(f"Invalid read mode: {read_mode}")

# Function to open the event log
def open_event_log(server, log_type):
    try:
        return win32evtlog.OpenEventLog(server, log_type)
    except Exception as e:
        print(f"Error opening event log: {e}")
        return None

# Function to read events from the log
def read_events(handle, event_type, events_retrieved, batch_size=100):
    try:
        # Read the next batch of events
        return win32evtlog.ReadEventLog(handle, event_type, events_retrieved, batch_size)
    except Exception as e:
        print(f"Error reading events: {e}")
        return []

# Function to process and print events
def process_events(events, event_type_flags):
    for event in events:
        if event.EventType & event_type_flags:
            print(f"Event Category: {event.EventCategory}")
            print(f"Time Generated: {event.TimeGenerated}")
            print(f"Source: {event.SourceName}")
            print(f"Message: {event.StringInserts}")
            print("=" * 50)

# Function to close the event log handle
def close_event_log(handle):
    try:
        win32evtlog.CloseEventLog(handle)
    except Exception as e:
        print(f"Error closing event log: {e}")

# Main function to handle event log reading and processing
def main():
    print ('Windows Log Parser')

    # Call parse_args to handle argument parsing
    args = parse_args()

    # Get the read flags based on the user input
    read_flags = get_read_flags(args.read_mode)

    # Get the event type flags based on user input
    event_type_flags = get_event_type_flags(args.event_types)
    
    # Define the Target System
    server = 'localhost'

    # Select The type of windows event log : System, Application, Security
    log_type = 'Application'   

    # Open the event log
    handle = open_event_log(server, log_type)
    if handle is None:
        return

    # Read events in a loop until no more events are available
    events_retrieved = 0
    batch_size = 100
    while True:
        events = read_events(handle, read_flags, events_retrieved, batch_size)
        
        if not events:
            print("No more events to read.")
            break
        
        process_events(events, event_type_flags)
        
        events_retrieved += len(events)

    # Close the event log handle
    close_event_log(handle)



if __name__ == '__main__':
    main()