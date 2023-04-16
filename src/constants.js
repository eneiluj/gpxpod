import { translate as t } from '@nextcloud/l10n'

export const TRACK_SORT_ORDER = {
	name: {
		value: 0,
		label: t('gpxpod', 'Name'),
	},
	date: {
		value: 1,
		label: t('gpxpod', 'Date'),
	},
	distance: {
		value: 2,
		label: t('gpxpod', 'Total distance'),
	},
	duration: {
		value: 3,
		label: t('gpxpod', 'Total duration'),
	},
	elevationGain: {
		value: 4,
		label: t('gpxpod', 'Cumulative elevation gain'),
	},
}

export const COLOR_CRITERIAS = {
	none: {
		id: 0,
		label: t('gpxpod', 'None'),
	},
	elevation: {
		id: 1,
		label: t('gpxpod', 'Elevation'),
	},
	speed: {
		id: 2,
		label: t('gpxpod', 'Speed'),
	},
	pace: {
		id: 3,
		label: t('gpxpod', 'Pace'),
	},
	traveled_distance: {
		id: 4,
		label: t('gpxpod', 'Traveled distance'),
	},
}

// hue: RED: 0, YELLOW: 60, GREEN: 120, CYAN: 180, BLUE: 240, MAGENTA, 300
// steps of Pi/3 between red, green and blue
export function getColorGradientColors(startHue = 0, endHue = 120, percentStep = 0.1) {
	const hueDiff = endHue - startHue
	const result = []
	for (let i = 0; i <= 1; i += percentStep) {
		result.push('hsl(' + (startHue + i * hueDiff).toString(10) + ', 100%, 50%)',)
	}
	return result
	/*
	return [
		'hsl(' + maxHue + ', 100%, 50%)',
		'hsl(' + (minHue + 0.9 * hueDiff).toString(10) + ', 100%, 50%)',
		'hsl(' + (minHue + 0.8 * hueDiff).toString(10) + ', 100%, 50%)',
		'hsl(' + (minHue + 0.7 * hueDiff).toString(10) + ', 100%, 50%)',
		'hsl(' + (minHue + 0.6 * hueDiff).toString(10) + ', 100%, 50%)',
		'hsl(' + (minHue + 0.5 * hueDiff).toString(10) + ', 100%, 50%)',
		'hsl(' + (minHue + 0.4 * hueDiff).toString(10) + ', 100%, 50%)',
		'hsl(' + (minHue + 0.3 * hueDiff).toString(10) + ', 100%, 50%)',
		'hsl(' + (minHue + 0.2 * hueDiff).toString(10) + ', 100%, 50%)',
		'hsl(' + (minHue + 0.1 * hueDiff).toString(10) + ', 100%, 50%)',
		'hsl(' + minHue + ', 100%, 50%)',
	]
	*/
}

export function getColorHueInInterval(startHue = 0, endHue = 120, weight) {
	const hueDiff = endHue - startHue
	return startHue + (weight * hueDiff)
}
