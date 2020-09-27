## Prerequisites

* Ruby 2.5+ ([rvm](https://rvm.io/) recommended to manage Ruby environments)
* Python 3.6+ ([Anaconda](https://www.anaconda.com/distribution/) recommended to manage Python environments)
* Node.js 8.16.0+
* Yarn 1.x+

WhatsOpt is a [Ruby on Rails](https://rubyonrails.org/) application, as such it follows typical installation procedure for such application. 
A lot of material about RoR applications installation and configuration is available [out there](https://www.google.com/search?q=ruby+on+rails+application+installation).

## Development setup

WhatsOpt rails application setup:
<pre>
  git clone https://github.com/OneraHub/WhatsOpt
</pre>
WhatsOpt command line interface setup, namely wop:
<pre>
  pip install wop
</pre>
The <code>wop</code> package pulls also Python dependencies used by WhatsOpt application, specially the [OpenMDAO framework](https://openmdao.org) which is currently the execution framework used by WhatsOpt. 

Though not stricly required to run WhatsOpt, some features relies also on the following Python packages:

* [SMT](https://smt.readthedocs.io/): enable design of experiments and metamodels creation
* [SALib](https://salib.readthedocs.io/): enable sensitivity analysis operations
* [Apache Thrift](https://thrift.apache.org/): enable server creation and remote operations on local network
* [OpenTURNS](https://openturns.org): enable uncertain variables operations 

<pre>
  pip install smt salib thrift
</pre>
To enable server code generation, you will have to install Apache Thrift compiler as well.

This is the typical development mode of a Rails application, it is simpler to install than a typical production server (with a full-blown web server and database engine). It will allow you to get started with WhatsOpt in your local environment.    

<pre>
  cd WhatsOpt
  bundle install
  cp config/configuration.yml.example config/configuration.yml
  cp config/database.yml.example config/database.yml
  rails db:migrate
  rails db:seed
  rails s -b 0.0.0.0
</pre>

Then you can visit the http://localhost:3000 url and log in with the default user login/passwd: <code>whatsopt</code>/<code>whatsopt</code>

You can also run tests with:

<pre>
  rails test
</pre>

## Production setup
Ruby on Rails ecosystem allows various options for application server configuration and deployment. Refer to related Ruby on Rails documentation to know your deployment options.

The guide lines summarized below are related to the deployment of WhatsOpt on [ONERA server](https://ether.onera.fr/whatsopt). It relies on:

* Apache Server
* Passenger (aka module for rails)
* MySQL

Once those prerequisites are installed on your server, you have to fit:

* <code>config/environments/configuration.yml</code>
* <code>config/environments/database.yml</code>
* <code>config/environments/production.rb</code>
* <code>config/environments/ldap.yml</code> (if needed) 

For deployment in production, capistrano utility is used, you have to fit to your needs the following files:

* <code>config/deploy.rb</code>
* <code>config/deploy/production.rb</code>

then the deployment is one command line away:
<pre>
  cap production deploy
</pre>


