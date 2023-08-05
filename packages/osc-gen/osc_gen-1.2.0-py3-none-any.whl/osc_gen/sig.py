#!/usr/bin/env python3
"""
Copyright 2019 Harvey Ormston

This file is part of osc_gen.

    osc_gen is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    osc_gen is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with osc_gen.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np

from osc_gen import dsp


class SigGen(object):
    """ Signal Generator """

    def __init__(self, num_points=128, amp=1.0, phase=0, harmonic=0):
        """ Init """

        self.num_points = num_points
        self.amp = amp
        self.harmonic = harmonic
        self.phase = phase

    @property
    def _base(self):
        """ Generate the base waveform cycle, a sawtooth or ramp from -1 to 1
        """

        repeats = self.harmonic + 1
        normalized_phase = self.phase / (2 * np.pi)
        start = normalized_phase
        stop = start + repeats

        wave = np.linspace(start, stop, num=self.num_points, dtype=np.float32)

        # wrap and shift to +/- 1
        wrap_threshold = np.finfo(np.float32).eps
        wave %= 1 + wrap_threshold
        wave *= 2
        wave[wave > 1] -= 2

        return wave

    def saw(self):
        """ Generate a sawtooth wave cycle """

        return self.amp * self._base

    def tri(self):
        """ Generate a triangle wave cycle """

        # shift to start at 0
        shift = -self.num_points // (4 * (self.harmonic + 1))

        return np.roll(self.amp * self.arb((np.abs(self._base[:-1]))), shift)

    def pls(self, width):
        """ Generate a pulse wave cycle

            @param width float : Pulse width or duty cycle, between -1 and 1,
                where 0 corresponds to a square wave.
        """

        pls = self._base
        pls[np.where(pls < width)[0]] = -1.
        pls[np.where(pls >= width)[0]] = 1.

        return self.amp * pls

    def sqr(self):
        """ Generate a square wave cycle """

        return self.pls(0)

    def sin(self):
        """ Generate a sine wave cycle """

        return self.amp * self.arb(np.sin(np.pi * self._base[:-1]))

    def arb(self, data):
        """ Generate an arbitrary wave cycle. The provided data will be
        interpolated, if possible, to occupy the correct number of samples for
        a single cycle at our reference frequency and then normalized and
        scaled as appropriate.

        @param data seq : A sequence of samples representing a single cycle
            of a wave
        """

        try:
            dtype = type(data)
            if not isinstance(data, np.ndarray):
                data = np.array(list(data)).astype(np.float32)
        except ValueError:
            raise ValueError("Expected a sequence of data, got type {}.".format(dtype))

        if data.size == self.num_points:
            return data

        interp_y = data
        num = interp_y.size
        interp_x = np.linspace(0, num, num=num)
        interp_xx = np.linspace(0, num, num=self.num_points)
        interp_yy = np.interp(interp_xx, interp_x, interp_y)
        dsp.normalize(interp_yy)

        return interp_yy


def morph(waves, new_num):
    """ Take a number of wave cycles and generate a higher number of wave cycles
        where the original waves are linearly interpolated from one to the next
        to fill in the gaps.

        @param waves sequence : A sequence of wave cycles
        @param new_num int : The reuqired number of wave cycles in the new
            seuqence
    """

    inp = list(waves)
    inp_num = len(inp)

    if inp_num >= new_num:
        msg = "Can't morph a group into a smaller or equal group ({0} to {1})"
        raise ValueError(msg.format(inp_num, new_num))

    if inp_num < 2:
        msg = "Can't morph between less than 2 signals ({0})"
        raise ValueError(msg.format(inp_num))

    if inp_num == 2:
        return _morph_two(inp[0], inp[1], new_num)

    ranges = _detrmine_morph_ranges(inp_num, new_num)

    return _morph_many(inp, ranges)


def _detrmine_morph_ranges(inp_num, new_num):
    """ Find a set of integer gaps sizes between two set sizes

        @param inp_num int : The original set size
        @param new_num int : The new set size
    """

    gap_num = inp_num - 1
    gap_val = int(round(float(new_num) / gap_num, 0))
    ranges = [gap_val if j == 0 else gap_val + 1 for j in range(gap_num)]
    k = -1
    while sum(ranges) < new_num + gap_num - 1:
        ranges[k] += 1
        k -= 1
    while sum(ranges) > new_num + gap_num - 1:
        ranges[k] -= 1
        k -= 1

    return ranges


def _morph_many(waves, gaps):
    """ Morph between more then two sequences

        @param waves sequence : A sequence of wave cycles
        @param gaps sequence : The size of the gap between each pair of cycles
    """

    morphed = []
    prev_wave = None
    i = 0
    for curr_wave in waves:
        if prev_wave is not None:
            if i:
                start = 1
            else:
                start = 0

            morphed.extend(
                [x for x in _morph_two(
                    prev_wave, curr_wave, gaps[i])][start:])
            i += 1

        prev_wave = curr_wave

    return morphed


def _morph_two(wave_one, wave_two, new_num):
    """ Morph between two wave cycles.

        @param a sequence : The first wave cycle
        @param b sequence : The second wave cycle
        @param n int : The reuqired number of wave cycles in the new seuqence
    """

    alphas = (s / (new_num - 1.0) for s in range(new_num))

    return [wave_one * (1 - m) + wave_two * m for m in alphas]
