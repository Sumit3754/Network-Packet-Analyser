import pyshark

def capture_packets(interface):
    print(f"Starting packet capture on interface: {interface}")
    try:
        capture = pyshark.LiveCapture(interface=interface)
        for packet in capture.sniff_continuously(packet_count=10):  # Capture 10 packets
            print(f"Packet: {packet}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    interface = input("Enter the network interface (e.g., Wi-Fi, Ethernet): ")
    capture_packets(interface)
