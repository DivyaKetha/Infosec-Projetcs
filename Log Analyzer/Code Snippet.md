## 🔧 Code Snippet

```python
def analyze_logs(file_path, threshold=3):
    """
    Analyze log file for failed login attempts
    
    Args:
        file_path (str): Path to log file
        threshold (int): Number of attempts to trigger alert
    
    Returns:
        dict: IP addresses with attempt counts
    """
    ip_count = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            if "Failed password" in line:
                parts = line.split(" ")
                ip = parts[-1].strip()
                ip_count[ip] = ip_count.get(ip, 0) + 1
    
    return ip_count
```
