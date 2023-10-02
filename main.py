import subprocess



def main():

    subprocess.run(["./build/SingleFrameDetector_dm",
     "f7a4efcc-ce0d-458b-a158-da06a4308155_ovi.jpg",
     "/media/sd/objectDetection/netectorV2/models/damoyolo_tinynasL20_Nl.onnx_b1_gpu0_fp32.engine",
                    ])

if __name__ == "__main__":
    main() 