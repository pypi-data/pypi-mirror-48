cwlVersion: v1.0
class: CommandLineTool

requirements:
- class: InlineJavascriptRequirement
  expressionLib:
  - var default_output_filename = function() {
        return inputs.input_bed.location.split('/').slice(-1)[0].split('.').slice(0,-1).join('.')+".bb";
    };
  - var get_bed_type = function() {
        if (inputs.input_bed.location.split('.').slice(-1)[0].toLowerCase() == "narrowpeak"){
            return "bed6+4";
        } else if (inputs.input_bed.location.split('.').slice(-1)[0].toLowerCase() == "broadpeak"){
            return "bed6+3";
        } else {
            return null;
        }
    };
  - var get_bed_template = function() {
        if (inputs.input_bed.location.split('.').slice(-1)[0].toLowerCase() == "narrowpeak"){
            return "narrowpeak.as";
        } else if (inputs.input_bed.location.split('.').slice(-1)[0].toLowerCase() == "broadpeak"){
            return "broadpeak.as";
        } else {
            return null;
        }
    };
- class: InitialWorkDirRequirement
  listing:
    - entryname: narrowpeak.as
      entry: |
        table narrowPeak
        "BED6+4 Peaks of signal enrichment based on pooled, normalized (interpreted) data."
        (
          string  chrom;        "Reference sequence chromosome or scaffold"
          uint    chromStart;   "Start position in chromosome"
          uint    chromEnd;     "End position in chromosome"
          string  name;	        "Name given to a region (preferably unique). Use . if no name is assigned"
          uint    score;        "Indicates how dark the peak will be displayed in the browser (0-1000) "
          char[1] strand;       "+ or - or . for unknown"
          float   signalValue;  "Measurement of average enrichment for the region"
          float   pValue;       "Statistical significance of signal value (-log10). Set to -1 if not used."
          float   qValue;       "Statistical significance with multiple-test correction applied (FDR -log10). Set to -1 if not used."
          int     peak;         "Point-source called for this peak; 0-based offset from chromStart. Set to -1 if no point-source called."
        )
    - entryname: broadpeak.as
      entry: |
        table broadPeak
        "BED6+3 Peaks of signal enrichment based on pooled, normalized (interpreted) data."
        (
          string  chrom;        "Reference sequence chromosome or scaffold"
          uint    chromStart;   "Start position in chromosome"
          uint    chromEnd;     "End position in chromosome"
          string  name;	        "Name given to a region (preferably unique). Use . if no name is assigned."
          uint    score;        "Indicates how dark the peak will be displayed in the browser (0-1000)"
          char[1] strand;       "+ or - or . for unknown"
          float   signalValue;  "Measurement of average enrichment for the region"
          float   pValue;       "Statistical significance of signal value (-log10). Set to -1 if not used."
          float   qValue;       "Statistical significance with multiple-test correction applied (FDR -log10). Set to -1 if not used."
        )


hints:
- class: DockerRequirement
  dockerPull: biowardrobe2/ucscuserapps:v358

inputs:

  bed_type:
    type:
      - "null"
      - string
    inputBinding:
      position: 5
      prefix: -type=
      separate: false
      valueFrom: |
        ${
            if (self == ""){
              return get_bed_type();
            } else {
              return self;
            }
        }
    default: ""
    doc: |
      Type of BED file in a form of bedN[+[P]]. By default bed3 to three required BED fields

  bed_template:
    type:
      - "null"
      - string
      - File
    inputBinding:
      position: 6
      prefix: -as=
      separate: false
      valueFrom: |
        ${
            if (self == ""){
              return get_bed_template();
            } else {
              return self;
            }
        }
    default: ""
    doc: |
      For non-standard "bedPlus" fields put a definition of each field in a row in AutoSql format.
      By default includes only three required BED fields: chrom, chromStart, chromEnd

  block_size:
    type:
      - "null"
      - int
    inputBinding:
      position: 7
      prefix: -blockSize=
      separate: false
    doc: |
      Number of items to bundle in r-tree.  Default 256

  items_per_slot:
    type:
      - "null"
      - int
    inputBinding:
      position: 8
      prefix: -itemsPerSlot=
      separate: false
    doc: |
      Number of data points bundled at lowest level. Default 512

  unc:
    type:
      - "null"
      - boolean
    inputBinding:
      position: 9
      prefix: '-unc'
    doc: |
      If set, do not use compression

  tab_sep:
    type:
      - "null"
      - boolean
    inputBinding:
      position: 10
      prefix: '-tab'
    doc: |
      If set, expect fields to be tab separated, normally expects white space separator

  extra_index:
    type:
      - "null"
      - string
    inputBinding:
      position: 11
      prefix: -extraIndex=
      separate: false
    doc: |
      Makes an index on each field in a comma separated list extraIndex=name and extraIndex=name,id are commonly used

  size_2bit:
    type:
      - "null"
      - boolean
    inputBinding:
      position: 12
      prefix: -sizesIs2Bit=
      separate: false
    doc: |
      If set, the chrom.sizes file is assumed to be a 2bit file

  input_bed:
    type:
      - File
    inputBinding:
      position: 20
    doc: |
      Input BED file

  chrom_length_file:
    type:
      - File
    inputBinding:
      position: 21
    doc: |
      Chromosome length files

  output_filename:
    type:
      - "null"
      - string
    inputBinding:
      position: 22
      valueFrom: |
        ${
            if (self == ""){
              return default_output_filename();
            } else {
              return self;
            }
        }
    default: ""
    doc: |
      Output filename


outputs:
  bigbed_file:
    type: File
    outputBinding:
      glob: |
        ${
          if (inputs.output_filename == ""){
            return default_output_filename();
          } else {
            return inputs.output_filename;
          }
        }


baseCommand: ["bedToBigBed"]