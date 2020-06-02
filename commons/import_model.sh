#/bin/bash


[ $# -lt 1 ] && echo "A name of a BIGG model is needed." && exit 1
BASEDIR="../models/"
model=$1 #"iLB1027_lipid"

DIR="$BASEDIR/$model"
CONFIG="$DIR/config_$model.json"
URL="http://bigg.ucsd.edu/static/models/$model.json"

[ ! -d $DIR ] && mkdir $DIR
if [ ! -f $DIR/$model.json ] 
then
echo '{
"url": "'$URL'",
"modo": "real",
"sparse": "sparse.txt",
"reversibles": "reversibles.txt",
"bloqueadas": "bloqueadas.txt",
"matrix_file": "densa.txt",
"runs": 50,
"loops" : 2000,
"target" : "ejemploReact",
"random" : "s",
"verbose": "False"
}' > $CONFIG

fi

echo "Downloading ${model}.json  ..."
curl $URL > $DIR/$model.json 

echo "From JSON -> sparse ..."
/usr/bin/python json2sparse.py  --config $CONFIG
echo "From JSON -> reversibles ..."
/usr/bin/python json2reversibles.py  --config $CONFIG
echo "From sparse + reversibles -> numpy's format dense matrix..."
/usr/bin/python dense.py  --config $CONFIG

