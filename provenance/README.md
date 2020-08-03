## Generating DataLog files form the work flow models

(Clingo can be installed [here](https://potassco.org/doc/start/))

From the workflow file, extract the graphviz DOT file, and grep the edges

```
$ yw graph yesWorkFlow/dish.py | grep -e "->" > provenance/dish_edges.lp
```

From there, you can recreate the provenance in a datalog file. 
To run the provenance queries: 

```
$ clingo provenance/Provenance_Queries.txt
```