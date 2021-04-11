rm var/history.json
echo "{\"history\": []}" > var/history.json
rm types/__pycache__ -rf
rm temp/__pycache__ -rf
rm mod/__pycache__ -rf
rm kernel/__pycache__ -rf
rm data -rf
mkdir data
echo "" > data/.dontdelete
rm cpkg/fargparse/__pycache__ -rf
rm bin/__pycache__ -rf
rm .vscode -rf
rm __pycache__ -rf

