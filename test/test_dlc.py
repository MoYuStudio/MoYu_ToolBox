
import ctypes

# Load the Steam API library
steam_api = ctypes.cdll.LoadLibrary("steam_api.dll")

# Define the AppId_t type
AppId_t = ctypes.c_uint32

# Define the BIsDlcInstalled function signature
BIsDlcInstalled_func = steam_api.SteamAPI_ISteamApps_BIsDlcInstalled
BIsDlcInstalled_func.restype = ctypes.c_bool
BIsDlcInstalled_func.argtypes = [AppId_t]

# Example usage
app_id = 2384490  # Replace with the AppID of your DLC
is_installed = BIsDlcInstalled_func(app_id)
print(f"Is DLC installed: {is_installed}")