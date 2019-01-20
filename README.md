How to create custom rpm for your application
=============================================
1. Install the development environment
   yum install -y rpmdevtools rpmlint

2. Creat folder structure by running below command
   rpmdev-setuptree

   mkdir myscript-1.0/
   vim myscript-1.0/myscript.sh
   Edit the myscript.sh with content
   #!/bin/bash"Hello It's my first rpm!!!"
   tar czvf SOURCES/myscript-1.0.tar.gz myscript-1.0/
   chmod +x myscript-1.0/myscript.sh 
   rpmdev-newspec SPECS/myscript.spec
   
3. Command to create the rpm packages
 
   rpmbuild -bb SPECS/myscript.spec 
  
4. RPM will be careted and placed into the directory
   Path=>ls RPMS/i686/myscript-1.0-1.i686.rpm 

5. Install the rpm package
   rpm -ivh RPMS/i686/myscript-1.0-1.i686.rpm

6. Execute the script by running below script installed from above rpm
   /opt/myscript/myscript.sh 
   Output: Hello It's my first rpm!!!

   


