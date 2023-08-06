# Copyright Jonathan Tremesaygues (2019)
#
# Jonathan Tremesaygues <jonathan.tremesaygues@slaanesh.org>
#
# This software is a computer program whose purpose is to [describe
# functionalities and technical features of your software].
#
# This software is governed by the CeCILL-B license under French law and
# abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL-B
# license as circulated by CEA, CNRS and INRIA at the following URL
# "http://www.cecill.info".
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# In this respect, the user's attention is drawn to the risks associated
# with loading,  using,  modifying and/or developing or reproducing the
# software by the user in light of its specific status of free software,
# that may mean  that it is complicated to manipulate,  and  that  also
# therefore means  that it is reserved for developers  and  experienced
# professionals having in-depth computer knowledge. Users are therefore
# encouraged to load and test the software's suitability as regards their
# requirements in conditions enabling the security of their systems and/or
# data to be ensured and,  more generally, to use and operate it in the
# same conditions as regards security.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL-B license and that you accept its terms.
from ..config import AggregateConfig, BooleanConfig
from .lut import LUTConfig
from ..direction import Direction
from ..module import (
    Module,
    Port,
    RangeDescription,
    NewLine,
    Comment,
    Wire,
    ModuleInstantiation,
    Parameter,
    PortConnection,
    Assign,
)


class LEConfig(AggregateConfig):
    def __init__(self, lut_size):
        self.lut = LUTConfig(lut_size)
        self.enable_dff = BooleanConfig()

        super().__init__([self.lut, self.enable_dff])


def get_le_module(lut_size):
    config = LEConfig(lut_size)

    module = Module(
        "LogicElement",
        description="A look-up table followed by an optional DFF",
        ports=[
            Port(
                "i_data_in",
                Direction.INPUT,
                width=lut_size,
                description="The input data",
            ),
            Port(
                "o_data_out", Direction.OUTPUT, description="The output data"
            ),
            Port("i_clk", Direction.INPUT, description="Clock signal"),
            Port(
                "i_set", Direction.INPUT, description="Synchronous set signal"
            ),
            Port(
                "i_nreset",
                Direction.INPUT,
                description="Synchronous reset signal, active low",
            ),
            Port("i_enable", Direction.INPUT, description="Enable signal"),
            Port(
                "i_config",
                Direction.INPUT,
                width=config.width,
                description="Configuration",
                range_descriptions=[
                    RangeDescription(
                        *config.get_range(config.lut),
                        "Configuration of the LUT",
                    ),
                    RangeDescription(
                        *config.get_range(config.enable_dff), "Use the DFF?"
                    ),
                ],
            ),
        ],
        body_parts=[
            NewLine(),
            Comment("Instantiate the LUT"),
            Wire("w_data_from_lut"),
            ModuleInstantiation(
                "LookUpTable",
                "c_lut",
                parameters=[Parameter("SIZE", lut_size)],
                port_connections=[
                    PortConnection("i_data_in", "i_data_in"),
                    PortConnection("o_data_out", "w_data_from_lut"),
                    PortConnection(
                        "i_config",
                        "i_config[{}:0]".format(config.lut.width - 1),
                    ),
                ],
            ),
            NewLine(),
            Comment("Instantiate the DFF"),
            Wire("w_data_from_dff"),
            ModuleInstantiation(
                "DFFSRE",
                "c_dff",
                port_connections=[
                    PortConnection("i_data_in", "w_data_from_lut"),
                    PortConnection("o_data_out", "w_data_from_dff"),
                    PortConnection("i_clk", "i_clk"),
                    PortConnection("i_set", "i_set"),
                    PortConnection("i_nreset", "i_nreset"),
                    PortConnection("i_enable", "i_enable"),
                ],
            ),
            NewLine(),
            Comment("Choose between the output of the LUT and the DFF"),
            Assign(
                "o_data_out",
                "i_config[{}] ? w_data_from_dff : w_data_from_lut".format(
                    config.width - 1
                ),
            ),
        ],
    )

    return module
