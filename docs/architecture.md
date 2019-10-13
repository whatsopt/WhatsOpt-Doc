# Architecture

## MDAO Domain Model

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

* _Discipline_: regular discipline
* _Analysis_: discipline containing an analysis
* _Function_: utiity pseudo-discipline allowing to compute synthetize quantity from other discipline outputs
* _MetaModel_: discipline which is implemented thanks to surrogate models

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

A connection links an output variable to a set of input variables a soon as variables have the same name.
Connection carries also a role property which defaults to:

* _parameter_ when the output variable is produced by the _Driver_
* _response_ when the input variable is consumed by the _Driver_
* _state_ otherwise 

A _parameter_ connection can be specialized as a _design variable_ connection.

A _response_ connection can be specialized as a:

* _min objective_ or _max objective_ to specify the response is an optimization objective
* _neg constraint_ or _eq constraint_ to specify the response as a negative or equality constraint

### Operations and result Cases

An _Operation_ on an analysis can be either an optimization or the execution of a design of experiments.
Results are input variables values (i.e. _Cases_) successivly set by the driver (optimizer or doe runner) and the 
corresponding output variables produced by the analysis evaluation.  

Special design of experiments Morris is distinguish as used to carryout special screening operation
thanks to Morris' method.

### MetaModel and Surrogates

A _MetaModel_ can be built out of a design of experiments operation results of a given analysis. 
It consists of a set of surrogate models, one _Surrogate_ being built for each scalar output variables of
metamodeled analysis. When the output variable is an array, one surrogate is built for each scalar components.

## Main Design choices

### Ruby on Rails

WhatsOpt is a [Ruby on Rails](http://https://rubyonrails.org/) application. 

To get started with WhatsOpt design, an understanding of the Ruby on Rails framework is mandatory as it explains
most of the purpose and layout of the WhatsOpt code.
See [Rails Guides](https://guides.rubyonrails.org/)    

Models classes corresponding to domain model can be found in [app/models](https://github.com/OneraHub/WhatsOpt/tree/master/app/models) directory. 

### Apache Thrift

The [RPC framework Apache Thrift](https://thrift.apache.org/) is used for two purposes:

* Server code generation: allows serve OpenMDAO compute methods of the various disciplines of an analysis.
* Ruby/Python communication between WhatsOpt backend and [Surrogate Modeling Toolbox library](https://github.com/SMTorg/smt) 

While the first item is detailed in [Projection section](#apache-thrift-server-projection), the second is the object
of the [surrogate_server directory](https://github.com/OneraHub/WhatsOpt/tree/master/surrogate_server) 
where a Thrift IDL interface allows to generate Python code for the server side while client code is generated
in [Ruby WhatsOpt library](https://github.com/OneraHub/WhatsOpt/tree/master/app/lib/whats_opt/surrogate_server) and
used by the [_SurrogateProxy_](https://github.com/OneraHub/WhatsOpt/tree/master/app/lib/whats_opt/surrogate_proxy.rb) class.  

## Projections

### OpenMDAO projection

The mapping between WhatsOpt domain model and the [OpenMDAO framework](https://openmdao.org) implementation is straightforward:

* _Analysis_ is mapped to _Group_
* _Discipline_ is mapped to _Component_
* _Operation_ is mapped to _Driver_ 

The code generation relies on Ruby template engine ERB (see app/lib/Whats_opt/templates directory) used by the [_OpenmdaoCodeGenerator_](https://github.com/OneraHub/WhatsOpt/blob/master/app/lib/whats_opt/openmdao_generator.rb)

Beside this generic part, WhatsOpt allows specify finer details about the projection in OpenMDAO terms. 
The idea here is to offer sufficient level of control to allow any required specialization at Python language level.
Indeed, at some point it is easier to write Python code than using a graphical interface which will not be able to handle
all cases anyway.

In WhatsOpt, on a specific page, the user is able to specify:

* whether the container OpenMDAO group is meant to be executed in parallel or not,
* which types of solvers and their parameterization are used,
* whether a discipline is an implicit or explicit OpenMDAO component,
* whether a discipline declares derivatives.

In practice, this is handled by the following classes [_OpenmdaoAnalysisImpl_, _OpenmdaoDisciplineImpl_ and _Solver_

### Apache Thrift Server projection 

The idea was to expose all the OpenMDAO <code>compute</code> methods of the disciplines of a given analysis on the local network.
When the server is started it listens on the port 31400. 
The client is either the WhatsOpt application itself client of the while analysis or a generated run script provided .
In the first case it allows to use operation drivers installed on the WhatsOpt server like optimizers.
In the second case it allows to call a discipline remotely, thus distributing discipline computations over the network. 

The analysis and discipline interface definitions are used to produce an appropriate Thrift IDL file 
which in turns, with the help of Thrift compiler, will produce the needed client/server code. 

The code generation is handled by the [_ServerGenerator_](https://github.com/OneraHub/WhatsOpt/blob/master/app/lib/whats_opt/server_generator.rb) class.

### CMDOWS projection

[CMDOWS](https://bitbucket.org/imcovangent/cmdows) is an XML format for multidisciplinary optimization domain.

The code generation is handled by the [_CmdowsGenerator_](https://github.com/OneraHub/WhatsOpt/blob/master/app/lib/whats_opt/cmdows_generator.rb) class.
