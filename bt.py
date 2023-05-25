import http.client
import json

#connects to the prompt endpoint and prints data
def promtFunc(system, prompt):
    conn = http.client.HTTPSConnection("dashboard.bitapai.io")
    payload = json.dumps({
    "system": system,
    "user": prompt
    })
    headers = {
    'Content-Type': 'application/json',
    #my individual api-key
    'X-API-KEY': 'your-key'
    }
    conn.request("POST", "/api/v1/prompt", payload, headers)
    res = conn.getresponse()
    data = res.read()
    #prints the result of the prompt
    print(data.decode("utf-8"))

def main():
    #System Inputs, which you can choose to use, feel free to add more to this dict
    system_inputs = {1: "Development",
                     2: "Investment",
                     3: "Academic",
                     4: "Joke",
                     5: "Poem",
                     6: "German",
                     7: "Bittensor",
                     8: ""}
    
    while True:
        print(system_inputs,"\n")
        system_choice = int(input(f"System(Wähle eine Nummer):"))
        system = system_inputs[system_choice]
        print(f"System = {system}")
        prompt = input("Prompt:")
        print("")
        #needs two variables, system = rough setting of the prompt, prompt = actual question
        promtFunc(system,prompt)
        
        print("*****************************************************************************************************\n")
main()
        