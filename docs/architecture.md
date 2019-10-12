# Architecture

## Object Model

### Analysis

WhatsOpt handles multidisciplinary analyses (analyses for short).
An analysis is composed with a list of disciplines which are connected through variables.

_Analysis_ and _Discipline_ follows a Composite/Component pattern.
An analysis can contain a discipline which can be in turn the container of another analysis.
Thus analyses can be arrange in hierarchy of nested analyses forming a tree, 
where root analyses are the entry point for the user.

### Discipline

A _Discipline_ represents an execution unit typically dedicated to a numerical model of a physical domain 
(aerodynamics, structure, propulsion, ...). Disciplines have named inputs and named outputs also called
input and output variables. Disciplines can have the following stereotype :

* Discipline: regular discipline
* Analysis: discipline containing an analysis
* Function: pseudo-discipline allowing to compute synthetize quantity from other discipline outputs
* MetaModel: discipline which is implemented thanks to surrogate models

A special pseudo-discipline is the _Driver_, unique in the analysis, first in the list of discipline, it represents
either the user or a client program of the analysis on behalf of the user (e.g. an optimizer or a doe runner).

### Variable

A _Variable_ in WhatsOpt act as a named connector of a _Discipline_ being either an input or an output.
Another way to consider it is that a Discipline consumes (resp. produces) input variables  (resp. output variables). 
Variables are automatically connected as soon as they have the same name one being an input the other an output.

!!! note
    Names for output variables are unique within the analysis, corresponding to the fact that only one discipline
    can produce a given variable 

Beside its name a variable has the following properties:

* a type: either Float or Integer
* a shape: either a scalar or an array of 1 to 4 dimensions
* a description: free text to describe the variable
* an initial value (optional)
* a lower bound (optional)
* an upper bound (optional)

### Connection

A connection links an output variables to a set of input variables a soon as variables have the same name.
Connection carries also a role which default to:

* _parameter_ when the output variable is produced by the _Driver_
* _response_ when the input variable is consumed by the _Driver_
* _state_ otherwise 

A _parameter_ connection can be specialized as a _design variable_ connection.

A _response_ connection can be specialized as a:

* _min objective_ or _max objective_ to specify the response is an optimization objective
* _neg constraint_ or _eq constraint_ to specify the response as a negative or equality constraint

### Analysis Discipline

### MetaModel

### Surrogate

### OpenMDAO Implementation