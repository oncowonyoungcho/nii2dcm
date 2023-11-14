"""
nii2dcm entrypoint code and command line interface (CLI)
"""

import sys
import argparse
from pathlib import Path
from nii2dcm.run import run_nii2dcm
from nii2dcm._version import __version__


def cli(args=None):
    """
    Run nii2dcm via command line
    """
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="nii2dcm",
        description="nii2dcm - NIfTI file to DICOM conversion"
    )

    parser.add_argument("input_file", type=str, help="[.nii/.nii.gz] input NIfTI file or path")
    parser.add_argument("-o","--output_dir", type=str, help="[directory] output DICOM path")
    parser.add_argument("-d", "--dicom_type", type=str, default='MR',help="[string] type of DICOM. e.g. MR, CT, MR with SVR, etc.")
    parser.add_argument("-rt", "--rt_structure", action='store_true', help="[string] in the case of the input file is RT structure")
    parser.add_argument("-p", "--patient_name", type=str, help="[string] Patient name to be in DICOM file (Default: input file name)")
    parser.add_argument("-pid", "--patient_id", type=str, help="[string] Patient ID to be in DICOM file (Default: input file name)")
    parser.add_argument("-r", "--ref_dicom", type=str, help="[.dcm] Reference DICOM file for Attribute transfer")
    parser.add_argument("-v", "--version", action="version", version=__version__)

    args = parser.parse_args()

    input_file = Path(args.input_file)  # TODO: add check that file is .nii/.nii.gz

    if input_file.is_dir():
        input_files = list(input_file.glob('*.nii.gz'))
    elif input_file.is_file():
        input_files = [input_file]
        if not input_file.exists():
            print(f"Input file '{input_file}' not found")
            raise SystemExit(1)

    dicom_type = None
    if args.dicom_type is not None:
        dicom_type = args.dicom_type  # TODO: add check that supplied dicom_type is permitted

    
    if args.ref_dicom is not None:
        ref_dicom_file = Path(args.ref_dicom)   # TODO: add check that file is DICOM
    elif args.ref_dicom is None:
        ref_dicom_file = None

     
    # execute nii2dcm
    for fname in input_files:
        if not args.output_dir:
            output_dir = Path(str(fname).split('.nii')[0])
            output_dir.mkdir(parents=True, exist_ok=True)
        else:
            output_dir = Path(args.output_dir)
            
        if args.patient_name:
            patient_name = args.patient_name.split('.nii')[0]
        else:
            patient_name = output_dir.stem.split('.nii')[0]

        run_nii2dcm(
            fname,
            output_dir,
            patient_name,
            dicom_type,
            ref_dicom_file,
            args.rt_structure
        )


if __name__ == "__main__":
    sys.exit(cli())
