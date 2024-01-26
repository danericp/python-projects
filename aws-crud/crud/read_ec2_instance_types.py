from gateway import do_parse_json, do_setup_aws_client


def do_read_ec2_instance_types(json):
    json_data = do_parse_json(json)
    ec2_client = do_setup_aws_client(json_data, 'ec2')
    try:
        aws_out = ec2_client.describe_instance_types()
        if not aws_out:
            print("No EC2 instance types found.")
        else:
            print("=" * json_data["metadata"]["line-break-width"])
            print("List of EC2 Instance Types:")
            for instance_type in aws_out['InstanceTypes']:
                print(f"\tInstance Type: {instance_type['InstanceType']}")
                print(f"\t\tCurrentGeneration: {instance_type['CurrentGeneration']}")
                print(f"\t\tFreeTierEligible: {instance_type['FreeTierEligible']}")
                print(f"\t\tProcessorInfo: {instance_type['ProcessorInfo']}")
                print(f"\t\tVCpuInfo:")
                print(f"\t\t\tDefaultVCpus: {instance_type['VCpuInfo']['DefaultVCpus']}")
                print(f"\t\t\tDefaultCores: {instance_type['VCpuInfo']['DefaultCores']}")
                print(f"\t\t\tDefaultThreadsPerCore: {instance_type['VCpuInfo']['DefaultThreadsPerCore']}")
                if 'ValidCores' in instance_type['VCpuInfo'].keys():
                    print(f"\t\t\tValidCores: {instance_type['VCpuInfo']['ValidCores']}")
                if 'ValidThreadsPerCore' in instance_type['VCpuInfo'].keys():
                    print(f"\t\t\tValidThreadsPerCore: {instance_type['VCpuInfo']['ValidThreadsPerCore']}")
                print(f"\t\tMemoryInfo: {instance_type['MemoryInfo']}")
                print(f"\t\tInstanceStorageSupported: {instance_type['InstanceStorageSupported']}")
                print(f"\t\tNetworkInfo:")
                print(f"\t\t\tNetworkPerformance: {instance_type['NetworkInfo']['NetworkPerformance']}")
                print(f"\t\t\tMaximumNetworkInterfaces: {instance_type['NetworkInfo']['MaximumNetworkInterfaces']}")
                print(f"\t\t\tMaximumNetworkCards: {instance_type['NetworkInfo']['MaximumNetworkCards']}")
                print(f"\t\t\tIpv4AddressesPerInterface: {instance_type['NetworkInfo']['Ipv4AddressesPerInterface']}")
                print(f"\t\t\tIpv6AddressesPerInterface: {instance_type['NetworkInfo']['Ipv6AddressesPerInterface']}")
                print(f"\t\t\tIpv6Supported: {instance_type['NetworkInfo']['Ipv6Supported']}")
                print(f"\t\tSupportedBootModes: {instance_type['SupportedBootModes']}")
                print(f"\t\tNitroTpmSupport: {instance_type['NitroTpmSupport']}")
                print(f"\t\tEbsInfo:")
                if 'EbsOptimizedInfo' in instance_type['EbsInfo'].keys():
                    print(f"\t\t\tEbsOptimizedInfo: {instance_type['EbsInfo']['EbsOptimizedInfo']}\n")
    except ec2_client.exceptions.ClientError as e:
        print(f"ec2_client.exceptions.ClientError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
