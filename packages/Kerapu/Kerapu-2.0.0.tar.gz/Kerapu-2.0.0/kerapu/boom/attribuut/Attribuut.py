"""
Kerapu
"""
import abc

from kerapu.boom.boom_parameter import create_boom_parameter
from kerapu.lbz.Subtraject import Subtraject


class Attribuut:
    """
    Abstract klasse voor attributen.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, attribuut_id: int, boom_parameter_nummer: int):
        """
        Object constructor.

        :param int attribuut_id: Het ID van dit attribuut.
        :param int boom_parameter_nummer: Het ID van de boomparameter va dit attribuut.
        """
        self._attribuut_id = attribuut_id
        """
        Het ID van dit attribuut.

        :type: int
        """
        self._boom_parameter = create_boom_parameter(boom_parameter_nummer)
        """
        De boomparameter van dit attribuut.

        :type: BoomParameter
        """

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def tel(self, subtraject: Subtraject) -> int:
        """
        Geeft het aantal malen dat de boomparameter voldoet aan de voorwaarde van dit attribuut.

        :param Subtraject subtraject: Het subtraject.

        :rtype: int
        """
        pass

# ----------------------------------------------------------------------------------------------------------------------
