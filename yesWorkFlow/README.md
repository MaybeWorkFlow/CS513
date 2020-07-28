# Yes work flow model

## installation & creation
In order to generate the workflow models locally, you'll first need to install YesWorkFlow.
Instructions can be found [here](https://github.com/yesworkflow-org/yw-prototypes#1-check-installed-version-of-java).

For generating the workflow models via the openRefine Json, you'll need to install [or2ywtool](https://pypi.org/project/or2ywtool/)



To generate each model:
```

# Menu - Cleaned with OpenRefine

# Generate YW file
$ or2yw -i openRefine/Menu.json -o  yesWorkFlow/Menu.py -t parallel

# To get workflow png
$ or2yw -i openRefine/Menu.json -o yesWorkFlow/Menu_worflow.png -ot png -t parallel

# to generate GraphViz
$ yw graph yesWorkFlow/Menu.py > yesWorkFlow/Menu.gv

# To get pdf 
$ dot -Tpdf yesWorkFlow/Menu.py -o Menu.pdf



# MenuItem



# MenuPage - Cleaned with OpenRefine

# generate YW file
$ or2yw -i openRefine/MenuPage.json -o  yesWorkFlow/MenuPage.py -t parallel

# To get workflow png 
$ or2yw -i openRefine/MenuPage.json -o yesWorkFlow/MenuPage_worflow.png -ot png -t parallel


# Dish

$ yw graph yesWorkFlow/dish.py | dot -Tpng -o yesWorkFlow/Dish_workflow.png


```
