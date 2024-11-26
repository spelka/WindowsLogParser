# Windows Event Log Reader

This script allows you to read and filter Windows Event Logs based on event types and read modes.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x** installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **pywin32** package installed, which provides the `win32evtlog` module used to interact with Windows event logs.

### Installing pywin32:

To install `pywin32` using bash, you can run the following command:
```bash
pip install pywin32
```

To install `pywin32` using PowerShell, run the following command:
```powershell
pip install pywin32
```

## Running the Script

### Command Line Arguments

The script requires the following command-line arguments:

1. **`--log`**: The Windows Event Log to read from (e.g., `Application`, `System`, `Security`).
   - **Required**

2. **`--event_types`**: List of event types to filter for. You can specify one or more types from the following options:
   - `error`
   - `warning`
   - `information`
   - **Required**

3. **`--read_mode`**: The mode to use for reading the event logs. Valid options are:
   - `forwards`: Read the event logs in a forward direction.
   - `backwards`: Read the event logs in a backward direction.
   - **Required**

### Example Usage

Run the script from the command line with the appropriate arguments:

```bash
python read_event_logs.py --log Application --event_types error warning --read_mode forwards
```

```powershell
python read_event_logs.py --log Application --event_types error warning --read_mode forwards
```

This command will:
- Read from the **Application** event log.
- Filter for events of type **error** and **warning**.
- Use the **forwards** read mode to fetch logs.

### Help Command

To view the help text describing the arguments and their usage, run:

```bash
python read_event_logs.py --help
```

```powershell
python read_event_logs.py --help
```

## Troubleshooting

- Ensure you are running the script on a Windows machine with the necessary permissions to access event logs.
- If the `pywin32` package is not installed, you can install it using the command:
  ```bash
  pip install pywin32
  ```
  ```powershell
  pip install pywin32
  ```
- Make sure you specify the required arguments (`--log`, `--event_types`, and `--read_mode`), or the script will prompt you with the help text.

## License

This script is provided as-is for educational purposes. No warranty is provided.