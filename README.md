## The Purpose of this repo to setup ADK + GEMMA running on DMR
To Enable docker Model Runner we can use  

docker desktop enable model-runner --tcp=9000
If we get the error like - 
failed to update settings: settings format not recognized, unknown settings keys: [enableInferenceTCP]
C:\Users\[Your-Username]\AppData\Roaming\Docker\settings-store.json 
{
  "AutoDownloadUpdates": false,
 …….. 
  "EnableInference": true,
  "EnableInferenceTCP": true,
  "EnableInferenceTCPPort": 9000,
  "ExposeDockerAPIOnTCP2375": true,..... <output terminated> 

### Steps to run the ADK with GEMMA4 (considering windows environment) 

set OPENAI_API_BASE=http://localhost:9000/engines/v1
To verify 
curl http://localhost:9000/engines/v1/models

set GEMMA_MODEL=ai/gemma4:E4B

python -m venv .venv
.venv\Scripts\activate
(.venv) pip install google-adk

(.venv) C:\Users\cidco>adk web
