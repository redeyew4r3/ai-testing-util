import socket
import struct
import time

def capture_packets(interface, output_file):
    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except socket.error as e:
        print(f"Socket could not be created, error code: {e.args[0]}")
        print(f"Error message: {e.args[1]}")
        return

    try:
        with open(output_file, 'wb') as f:
            while True:
                raw_data, addr = s.recvfrom(65565)
                f.write(raw_data)
                print(f"Captured packet from {addr}")
    except KeyboardInterrupt:
        print("Stopping packet capture.")
    finally:
        s.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Packet Capture Utility")
    parser.add_argument("interface", help="Network interface to capture packets from")
    parser.add_argument("output_file", help="File to save captured packets")
    args = parser.parse_args()
    capture_packets(args.interface, args.output_file)