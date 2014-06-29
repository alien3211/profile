#!/usr/bin/perl -w
$data = `uptime`;
if($data =~ m/(days|dni)/)
{
    $file_up = system("/home/alan/my_project/./tmux_right_script");
}
else
{
    $file_up = system("/home/alan/my_project/./no_deys");
}
print $file_up;
