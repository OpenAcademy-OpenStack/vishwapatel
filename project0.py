import novaclient.v1_1.client as nova_client
import keystoneclient.v2_0.client as keystone_client
import glanceclient.v2.client as glance_client
import project_credentials

# Get required credentials from the project credentials file
keystone_credentials = project_credentials.get_keystone_credentials()
nova_credentials = project_credentials.get_nova_credentials()

# Instaniate Keystone and Glance clients
keystone = keystone_client.Client(**keystone_credentials)
glance_endpoint = keystone.service_catalog.url_for(
    service_type='image', endpoint_type='publicURL')
glance = glance_client.Client(
    glance_endpoint, token=keystone.auth_token)
nova = nova_client.Client(**nova_credentials)

# Go through the images list from Glance and find instances named ubuntu
# and then create VMs for those images
image_list = glance.images.list()
flavor = nova.flavors.find(name="m1.micro")

for image in image_list:
        if "ubuntu" in image["name"]:
                print "Image with 'ubuntu' in it: " + image["name"]
                nova.servers.create(name=image["name"],
                                    image=image,
                                    flavor=flavor)
