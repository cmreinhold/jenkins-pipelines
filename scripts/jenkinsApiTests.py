import jenkinsapi
from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://139.59.211.11:8080'
    return Jenkins(jenkins_url, username='admin', password='migato00')
    
def get_server_version():
    server = get_server_instance()
    return server.version

def get_latest_success_build(jobName):
    server = get_server_instance()
    job = server[jobName]
    lgb = job.get_last_good_build()
    return lgb.get_revision()

"""Get job details of each job that is running on the Jenkins instance"""
def get_job_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for job_name, job_instance in server.get_jobs():
        print ('Job Name: ' + str(job_instance.name))
        print ('Job Description: ' + str(job_instance.get_description()))
        print ('Is Job running: ' + str(job_instance.is_running()))
        print ('Is Job enabled: ' + str(job_instance.is_enabled()))

"""Disable a Jenkins job"""
def disable_job(job_name=None):
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    if (server.has_job(job_name)):
        job_instance = server.get_job(job_name)
        job_instance.disable()
        print ('---JOB---')
        print ('---Job name: ' + str(job_name))
        print ('---Is Job Enabled? ' + str(job_instance.is_enabled()))
    else: 
        print ('Job ' + str(job_name) + ' not found')

def get_plugin_details():
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    for plugin in server.get_plugins().values():
        print ("---- PLUGIN ---")
        print ("Short Name: " + str(plugin.shortName))
        print ("Long Name: " +  str(plugin.longName))
        print ("Version: " + str(plugin.version))
        print ("URL: "  + str(plugin.url))
        print ("Active: " + plugin.active)
        print ("Enabled: " + plugin.enabled)

if __name__ == '__main__':
    print get_server_version()
    print get_job_details()

