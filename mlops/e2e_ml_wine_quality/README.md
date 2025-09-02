## Notes, code Explanation and thought Process

code explanation
```
```
The line:
```
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
```

Explanation:

This configures the Python logging module to control how log messages are handled and displayed.

Parameters:

level=logging.INFO:
Sets the minimum severity of messages to handle.

logging.INFO means only messages with level INFO or higher (WARNING, ERROR, CRITICAL) will be shown.
Lower-level messages (like DEBUG) will be ignored.
format='[%(asctime)s]: %(message)s:':
Specifies how each log message should be formatted.

%(asctime)s: Inserts the timestamp when the log message was created.
%(message)s: Inserts the actual log message.
The format will look like:
[2025-09-02 12:34:56,789]: This is a log message:
Summary:
This line sets up logging so that all INFO and higher messages are printed, each prefixed with a timestamp and formatted as shown.

shortcut : ctrl H - find and replace in vscode