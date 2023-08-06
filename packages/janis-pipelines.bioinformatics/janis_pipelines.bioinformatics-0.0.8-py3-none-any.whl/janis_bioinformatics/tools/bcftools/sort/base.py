from abc import ABC
from typing import Dict, Any

from datetime import datetime
from janis import CommandTool, ToolInput, ToolOutput, File, Boolean, String, Int, InputSelector, Filename, ToolMetadata, \
    CaptureType
from janis.utils import get_value_for_hints_and_ordered_resource_tuple
from janis_bioinformatics.data_types import Vcf


CORES_TUPLE = [
    (CaptureType.key(), {
        CaptureType.CHROMOSOME: 2,
        CaptureType.EXOME: 2,
        CaptureType.THIRTYX: 2,
        CaptureType.NINETYX: 2,
        CaptureType.THREEHUNDREDX: 2
    })
]

MEM_TUPLE = [
    (CaptureType.key(), {
        CaptureType.CHROMOSOME: 16,
        CaptureType.EXOME: 16,
        CaptureType.THIRTYX: 16,
        CaptureType.NINETYX: 16,
        CaptureType.THREEHUNDREDX: 16
    })
]


class BCFToolsSortBase(CommandTool, ABC):

    def friendly_name(self) -> str:
        return "BCFTools Sort"

    @staticmethod
    def tool_provider():
        return "Samtools"

    @staticmethod
    def tool() -> str:
        return "BCFToolsSort"

    @staticmethod
    def base_command():
        return ['bcftools', 'sort']

    def cpus(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, CORES_TUPLE)
        if val: return val
        return 2

    def memory(self, hints: Dict[str, Any]):
        val = get_value_for_hints_and_ordered_resource_tuple(hints, MEM_TUPLE)
        if val: return val
        return 8

    def inputs(self):
        return [
            ToolInput("vcf", Vcf(), position=1, doc="The VCF file to sort"),
            # ToolInput("maxMem", String(optional=True), default=MemorySelector(suffix="G"), prefix="--max-mem", doc="(-m) maximum memory to use [768M]"),
            ToolInput("outputFilename", Filename(), prefix="--output-file", doc="(-o) output file name [stdout]"),
            ToolInput("outputType", String(optional=True), prefix="--output-type",
                      doc="(-O) b: compressed BCF, u: uncompressed BCF, z: compressed VCF, v: uncompressed VCF [v]"),
            ToolInput("tempDir", String(optional=True), prefix="--temp-dir",
                      doc="(-T) temporary files [/tmp/bcftools-sort.XXXXXX/]"),
        ]

    def outputs(self):
        return [
            ToolOutput("out", Vcf(), glob=InputSelector("outputFilename"))
        ]

    def metadata(self):
        return ToolMetadata(
            creator=None,
            maintainer=None, maintainerEmail=None,
            dateCreated=datetime(2019, 5, 9), dateUpdated=datetime(2019, 5, 9),
            institution=None, doi=None,
            citation=None,
            keywords=["BCFToolsSort"],
            documentationUrl="",
            documentation="""About:   Sort VCF/BCF file.
Usage:   bcftools sort [OPTIONS] <FILE.vcf>""")
