#!/usr/bin/env python3

import io
import os

from gv_utils import enums


ENCODING = 'utf8'
CSVSEP = ';'

SAMPLES = enums.CsvData.samples
TIMESTAMP = enums.CsvData.timestamp


def dumps(dictdata):
    csvbuffer = io.BytesIO()
    timestamp, samples = dictdata[TIMESTAMP], dictdata[SAMPLES]
    metrics = None
    for sampleid, sample in samples.items():
        if metrics is None:
            metrics = list(sample.keys())
            headers = [str(timestamp), ] + metrics
            csvbuffer.write(CSVSEP.join(headers).encode(ENCODING))
        csvbuffer.write(os.linesep.encode(ENCODING))
        values = [str(sampleid), ]
        for metric in metrics:
            value = sample.get(metric, -1)
            if isinstance(value, float):
                value = round(value)
            values.append(str(value))
        csvbuffer.write(CSVSEP.join(values).encode(ENCODING))
    return csvbuffer


def loads(csvbuffer):
    header = bytes.decode(csvbuffer.readline(), ENCODING).strip(os.linesep).split(CSVSEP)
    dictdata = {TIMESTAMP: int(header.pop(0))}
    samples = {}
    for line in csvbuffer.readlines():
        line = bytes.decode(line, ENCODING).strip(os.linesep).split(CSVSEP)
        sampleid = line.pop(0)
        sample = {}
        for i in range(len(header)):
            value = line[i]
            try:
                value = int(value)
            except ValueError:
                pass
            sample[header[i]] = value
        samples[sampleid] = sample
    dictdata[SAMPLES] = samples
    return dictdata
