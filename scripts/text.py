from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://139.59.211.11:8080'
    server = Jenkins(jenkins_url, username='admin', password='migato00')
    return server

if __name__ == '__main__':
    print get_server_instance().version
