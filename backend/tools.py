import json

# Tool definitions based on main.py schema format
TOOLS = [
    {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name",
                }
            },
            "required": ["location"],
        },
    },
    {
        "name": "set_alarm",
        "description": "Set an alarm for a specific time",
        "parameters": {
            "type": "object",
            "properties": {
                "hour": {
                    "type": "integer",
                    "description": "Hour of the day (0-23)",
                },
                "minute": {
                    "type": "integer",
                    "description": "Minute of the hour (0-59)",
                }
            },
            "required": ["hour", "minute"],
        },
    },
    {
        "name": "send_message",
        "description": "Send a text message to a contact",
        "parameters": {
            "type": "object",
            "properties": {
                "recipient": {
                    "type": "string",
                    "description": "Name or number of the recipient",
                },
                "message": {
                    "type": "string",
                    "description": "The message content",
                }
            },
            "required": ["recipient", "message"],
        },
    },
    {
        "name": "play_music",
        "description": "Play a specific song, artist, or genre",
        "parameters": {
            "type": "object",
            "properties": {
                "song": {
                    "type": "string",
                    "description": "Name of the song, artist, or playlist",
                }
            },
            "required": ["song"],
        },
    },
    {
        "name": "set_timer",
        "description": "Set a timer for a specific duration in minutes",
        "parameters": {
            "type": "object",
            "properties": {
                "minutes": {
                    "type": "integer",
                    "description": "Duration of the timer in minutes",
                }
            },
            "required": ["minutes"],
        },
    },
    {
        "name": "create_reminder",
        "description": "Create a reminder for a specific task and time",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "What to remind about",
                },
                "time": {
                    "type": "string",
                    "description": "When to remind",
                }
            },
            "required": ["title", "time"],
        },
    },
    {
        "name": "search_contacts",
        "description": "Search for a contact's information",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Name of the person to search for",
                }
            },
            "required": ["query"],
        },
    },
    {
        "name": "open_app",
        "description": "Open an application on the device",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {
                    "type": "string",
                    "description": "Name of the application",
                }
            },
            "required": ["app_name"],
        },
    },
    {
        "name": "make_call",
        "description": "Make a phone call to a contact",
        "parameters": {
            "type": "object",
            "properties": {
                "contact": {
                    "type": "string",
                    "description": "Name or number to call",
                }
            },
            "required": ["contact"],
        },
    }
]

def simulate_action(function_name: str, arguments: dict) -> dict:
    """Simulates an action and returns a formatted JSON result for the frontend."""
    
    summary = ""
    emoji = "✅"
    
    if function_name == "get_weather":
        location = arguments.get("location", "Unknown")
        summary = f"🌤️ Checked weather in {location} (Mock 72°F)"
    
    elif function_name == "set_alarm":
        hour = arguments.get("hour", 0)
        minute = arguments.get("minute", 0)
        # Format time properly (e.g. 7:00 instead of 7:0)
        time_str = f"{hour:02d}:{minute:02d}"
        summary = f"⏰ Alarm set for {time_str}"
        
    elif function_name == "send_message":
        recipient = arguments.get("recipient", "Unknown")
        msg = arguments.get("message", "")
        summary = f"💬 Sent message to {recipient}: '{msg}'"
        
    elif function_name == "play_music":
        song = arguments.get("song", "something")
        summary = f"🎵 Playing {song}"
        
    elif function_name == "set_timer":
        minutes = arguments.get("minutes", 0)
        summary = f"⏱️ Timer set for {minutes} minutes"
        
    elif function_name == "create_reminder":
        title = arguments.get("title", "something")
        time_val = arguments.get("time", "later")
        summary = f"📌 Reminder set: {title} at {time_val}"
        
    elif function_name == "search_contacts":
        query = arguments.get("query", "Unknown")
        summary = f"📇 Found contact info for '{query}'"
        
    elif function_name == "open_app":
        app = arguments.get("app_name", "App")
        summary = f"📱 Opening {app}..."
        
    elif function_name == "make_call":
        contact = arguments.get("contact", "Unknown")
        summary = f"📞 Calling {contact}..."
        
    else:
        # Fallback for unknown tools
        summary = f"⚙️ Executed {function_name}"

    return {
        "tool": function_name,
        "summary": summary,
        "success": True 
    }

def simulate_actions(function_calls: list) -> list:
    """Process a list of function calls from the AI routing."""
    actions = []
    for call in function_calls:
        name = call.get("name")
        args = call.get("arguments", {})
        
        # If args is a JSON string instead of dict (happens with some models), parse it
        if isinstance(args, str):
            try:
                args = json.loads(args)
            except json.JSONDecodeError:
                args = {}
                
        if name:
             actions.append(simulate_action(name, args))
             
    return actions
