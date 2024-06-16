pipeline{
	agent any
	environment{
		registry = 'prc64/ejemplo-jenkins'
		registryCredentials = 'DockerHub'
		project = 'contenedor-python'
		projectVersion = '1.0'
		repository='https://github.com/prc64/prc64.git'
		repositoryCredentials = 'GitHub'
	}
	stages{
		stage('Limpiar workspace'){
			steps{
				cleanWs()
			}
		}
		stage('Checkout del codigo'){
			steps{
				script{
					git branch: 'main',
						credentials: repositoryCredentials,
						url: repository
				}
			}
		}
		stage('Construccion'){
			steps{
				script{
					dockerImage = docker.build registry
				}
			}
		}
		stage('Test'){
			steps{
				script{
					try{
						sh 'docker run --name $project $registry' 
					}finally{
						sh 'docker rm $project'
					}
				}
			}
		}
		stage('Despliegue'){
			steps{
				script{
					docker.withRegistry('', registryCredentials) {
						dockerImage.push()
					}
				}
			}
		}
		stage('Limpieza'){
			steps{
				script{
					sh 'docker rmi $registry'
				}
			}
		}			
	}
	post{
		always{
			echo 'Registrar Build'
		}
	}
}
