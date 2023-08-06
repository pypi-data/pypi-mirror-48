# caws  
  
configure AWS responsibly using profile names and environment vars.  
caws will write to an rc file setting AWS\_DEFAULT\_PROFILE to the profile name.   
if you do not have the rc file caws will create it for you.  
  
*you'll need to add "source .cawsrc" to your .bashrc or .bash\_profile*  
  
add new profiles using `$ aws configure --profile newname`   
  
### dependencies  
  
python3  
aws cli  
  
### usage  
  
`$ caws profilename`  
