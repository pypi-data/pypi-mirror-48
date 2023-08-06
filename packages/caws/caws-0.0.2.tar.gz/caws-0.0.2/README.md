# caws  
  
configure AWS responsibly using profile names and environment vars.  
  
rather than changing your AWS SDK credentials with `aws configure`, AWS suggests  
setting the ENV var AWS\_DEFAULT\_PROFILE to a [profile] in your ~/.aws/credentials.  
when set, this ENV var will over-ride the profile set with `aws configure`.  
  
caws will write to an rc file setting AWS\_DEFAULT\_PROFILE to the given profile name.   
if you do not have the rc file caws will create it for you.  
  
*you'll need to add `. .cawsrc` to your RC file (using bash: .bashrc or .bash\_profile)*  
  
add new profiles using `$ aws configure --profile newname`   
  
one benefit of using AWS\_DEFAULT\_PROFILE method instead of `aws configure` is the   
ability to add which AWS profile you're currently using to your command prompt.  
  
### dependencies  
  
python3  
aws cli  
  
### usage  
  
`$ caws profilename`  
