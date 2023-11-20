"""
IOD Module – CT Image

C.8.2.1
https://dicom.nema.org/medical/Dicom/current/output/chtml/part03/sect_C.8.2.html#sect_C.8.2.1

Note: Tags labelled ":missing:" are defined in the NEMA CT standard, but I have not found in real DICOMs exported from
an CT scanner.
"""


from nii2dcm.module import Module


class CTImage(Module):

    def __init__(self):
        super().__init__()

        self.module_type = 'CTImage'

        # ImageType
        # NEMA defines MR-specific ImageType terms here:
        # https://dicom.nema.org/medical/Dicom/current/output/chtml/part03/sect_C.8.3.html#sect_C.8.3.1.1.1
        # For now, will omit thereby inheriting parent value
        # self.ds.ImageType = ''
    
        self.ds.SamplesPerPixel = 1
    
        # PhotometricInterpretation
        # TODO: decide MONOCHROME1 or MONOCHROME2 as default
        # https://dicom.nema.org/medical/Dicom/current/output/chtml/part03/sect_C.7.6.3.html#sect_C.7.6.3.1.2
        self.ds.PhotometricInterpretation = 'MONOCHROME2'
    
        # PresentationLUTShape
        # depends on PhotometricInterpretation: https://dicom.innolitics.com/ciods/mr-image/general-image/20500020
        if self.ds.PhotometricInterpretation == 'MONOCHROME2':
            self.ds.PresentationLUTShape = 'IDENTITY'
        elif self.ds.PhotometricInterpretation == 'MONOCHROME1':
            self.ds.PresentationLUTShape = 'INVERSE'
    
        # Bits Allocated
        # defined to equal 16 for CT Image Module
        # https://dicom.nema.org/medical/Dicom/current/output/chtml/part03/sect_C.8.2.html#sect_C.8.2.1.1.4
        self.ds.BitsAllocated = 16
        self.ds.BitsStored = 16
        self.ds.HighBit = self.ds.BitsStored - 1

        self.ds.KVP = ''
        self.ds.AcquisitionNumber = ''
        self.ds.ScanOptions = ''
        self.ds.DataCollectionDiameter = ''
        self.ds.DataCollectionCenterPatient = ''
        self.ds.ReconstructionDiameter = ''
        self.ds.ReconstructionTargetCenterPatient = ''
        self.ds.DistanceSourcetoDetector = ''
        self.ds.DistanceSourcetoPatient = ''
        self.ds.GantryDetectorTilt = ''
        self.ds.TableHeight = ''
        self.ds.RotationDirection = ''
        self.ds.ExposureTime = ''
        self.ds.XRayTubeCurrent = ''
        self.ds.Exposure = ''
        self.ds.ExposureinµAs = ''
        self.ds.FilterType = ''
        self.ds.GeneratorPower = ''
        self.ds.FocalSpots = ''
        self.ds.ConvolutionKernel = ''
        self.ds.RevolutionTime = ''
        self.ds.SingleCollimationWidth = ''
        self.ds.TotalCollimationWidth = ''
        self.ds.TableSpeed = ''
        self.ds.TableFeedperRotation = ''
        self.ds.SpiralPitchFactor = ''
        self.ds.ExposureModulationType = ''
        self.ds.EstimatedDoseSaving = ''
        self.ds.CTDIvol = ''
        self.ds.CTDIPhantomTypeCodeSequence = ''
        self.ds.WaterEquivalentDiameter = ''
        self.ds.WaterEquivalentDiameterCalculationMethodCodeSequence = ''
        self.ds.ImageandFluoroscopyAreaDoseProduct = ''
        self.ds.CalciumScoringMassFactorPatient = ''
        self.ds.CalciumScoringMassFactorDevice = ''
        self.ds.EnergyWeightingFactor = ''
        self.ds.CTAdditionalXRaySourceSequence = ''
    
        # Currently omitting, but part of NEMA MR Image module:
        # NEMA Table 10-7 “General Anatomy Optional Macro Attributes”
    
        # Currently omitting, but part of NEMA MR Image module:
        # NEMA Table 10-25 “Optional View and Slice Progression Direction Macro Attributes”
    
        self.ds.IsocenterPosition = ''  # :missing:
        # self.ds.B1rms = ''

