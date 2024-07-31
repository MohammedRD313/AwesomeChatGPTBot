#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard Library Modules
import random
import string
import json
from typing import NoReturn, List, Dict, Union, Optional

# Related Third-Party Modules
import requests


# Open Ai Chat Provider 
def remix_ai(messages: List[Dict[str, str]]) -> Union[str, NoReturn]:
    """
    Chat completion for remix ai 
    
    Parameters:
        messages (List[Dict[str, str]]): Conversation history

    Returns:
        result (Union[str, None]): result or None in failure
    """
    # Base URL for provider API
    url: str = "https://api.freegpt4.tech/v1/chat/completions"
    
    # Request headers
    headers: Dict[str, str] = {
        "Accept": "text/event-stream",
        "Content-Type": "text/event-stream",
        "Accept-Language": "en",
        "Connection": "keep-alive",
        "Origin": "https://remix.ethereum.org",
        "Referer": "https://remix.ethereum.org/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    }
    
    # Request data
    data: typing.Dict[str, typing.Any] = {
        "messages": messages,
        "stream": True,
        "model": "gpt-4",
        "temperature": 0.5,
        "presence_penalty": 0,
        "frequency_penalty": 0,
        "top_p": 0.5,
    }

    # Try to send request or return None on failure
        # Try to send request or return None on failure
    try:
        # Get result from request
        res = requests.post(url=url, json=data, headers=headers).text
        
        # Get final streamed response
        gpt_result = ""
        for chuck in res.strip().split("\n\n")[:-1]:
            temp = json.loads(chuck.split("data: ")[1])
            try:
                gpt_result += temp['choices'][0]['delta']["content"]
            except:
                pass

        # Return response
        return gpt_result
        
    except:
        return None
