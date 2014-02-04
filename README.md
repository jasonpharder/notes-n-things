# notes-n-things

notes-n-things is the group Software Development project for Group 6

[insert super awesome description here]

Production Server:
Dev Server 1: [being used for...]
Dev Server 2: [being used for...]
Dev Server 3: [being used for...]
Dev Server 4: [being used for...]
Dev Server 5: [being used for...]

## Server set up
This part of the readme is for reference on how to properly set up the environment. Once the environment is finalized this information will not be strictly necessary and will function more for back up purposes (ie. if we lose the server image or something). For proper setup use the server image to create the server instace.

Server image: [insert image here when complete]

Get an instance:
Obviously before the server set up can happen, you a server instance. This is the relevant section from Alex Korn's setup tutorial: http://www.alexkorn.com/blog/2011/03/getting-php-mysql-running-amazon-ec2/

>Once you’ve gotten that set up, go to the AWS Management Console, and click on “Instances” in the Navigation panel. An >Instance is just a virtual server – so let’s create one! Click “Launch Instance” under “My Instances”, and select >“Basic 64-bit Amazon Linux AMI”. On the Instance Details phase, select “Micro” (which is Free tier eligible). Continue >until you need to enter the “Name” – if you don’t know what else to call it, just use “Web/DB server”.
>
>Next you create a Key Pair – this will be the credentials you’ll use to SSH into the box. The instructions here should >be fairly straightforward. Next is the Security Group, which will be used to specify the firewall used for your >instance. Feel free to use the default Group for now. Continue to the Review phase and launch it!
>
>You should now be able to SSH into your instance using your .pem file with ssh -i [FILE NAME].pem ec2-user@ec2-[IP >ADDRESS].compute-1.amazonaws.com. Alright, we’ve got a server up and running! However, you may notice that this server >has very little installed on it."

One 

##Setup Software:
This section will probably change substantially over the next day or two as the exact environment is finalized.

###Notes on syntax

<pre><code>
# implies the command should be run as root, this usually means via sudo.
  The one exception to this is editing the postgres conf file, which must be done as root as 
  for security reasons no users except root can even read those directories. 
  (to switch to root run $sudo su)

$ implies the command is run as the current user

postgres# means the command is run from within the postgres rdbms
</code></pre>

###postgres sql

<pre><code>
  #yum install postgresql9 postgresql9-server postgresql9-devel postgresql9-contrib postgresql9-docs
  #service postgresql initdb
  #vim /var/lib/pgsql/data/postgresql.conf
  uncomment the line listen_addresses = 'localhost'
  #exit
  #service postgresql start
  #su postgres
  $psql postgres
  postgres# \password postgres
  [enter pw twice] %we should have a unified password across servers for this
  postgres# \q
  //add in how to load the schema here
  $exit
</code></pre>

###git
<pre><code>
   #yum install git
</code></pre>

###nginx
<pre><code>
   #yum install nginx
   #mkdir /srv
   #mkdir /srv/html
   #vim /srv/html/index.html
   [write something like ‘OMG it works’]
   #vim /etc/nginx/nginx.conf
   [change line 52 (the root in location /) to be root /srv/html]
   #service start nginx
   //add python stuff here
</code></pre>

###Flask and plugins
<pre><code>
   #yum install gcc
   #yum install python-pip
   #pip install flask
   
   
</code></pre>
