# Easy API Keys

Just a simple way to add header api keys to protect fast when developers does have time to protect their API's endpoints.

By no means this is replacement for a true authentication, but at the speed of development, is better to deploy this kind of easy security in shared environments and to teach developers that is not that hard to do a little extra mile to consider and think about security.

Source the .env file as we should always create a single API key.

.env file

```bash
export APIKEY="79ada3fbb1de7a9e6333a0811a622d92f9f16c99d1d56ddca866ae2311702921"
```

This repo uses conda as environment:
```bash

conda create --name DevOpsEnv python=3.5

conda activate DevOpsEnv
```

Run

```bash
pip install -r requirements.txt

source .env

python EasyAPIKeys.py --webserver
```

Add ```click``` command line builder when possible, that adds more control to random programs that later on can be easily added to docker or other container virtualization technologies.
