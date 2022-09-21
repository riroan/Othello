import React, { useState } from 'react'
import styles from './main.module.scss'
import classnames from 'classnames/bind'
import Play from '../play'
const cx = classnames.bind(styles)

export default function Main() {
	const [first, setFirst] = useState(-1) // 선공 여부
	const [second, setSecond] = useState(0) // 구멍 선택
	const [arr, setArr] = useState([
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
	])
	const render = () => {
		const result = []
		for (let i = 0; i < 8; i++) {
			result.push(
				<div key={i} className={cx('row')}>
					{arr[i].map((j, ix) => {
						return (
							<button
								key={i * 8 + ix}
								className={cx('cell', arr[i][ix] === -1 ? 'disable' : 'able')}
								onClick={() => {
									arr[i][ix] = -1 - arr[i][ix]
									setArr(
										arr.map(i => {
											return i
										})
									)
								}}
							>
								Hi
							</button>
						)
					})}
				</div>
			)
		}
		return result
	}

	return (
		<div>
			<div className={cx(first === -1 ? '' : 'hidden', 'first')}>
				<button
					className={cx('firstButton')}
					onClick={() => {
						setFirst(0)
					}}
				>
					선공
				</button>
				<button
					className={cx('firstButton')}
					onClick={() => {
						setFirst(1)
					}}
				>
					후공
				</button>
			</div>
			<div className={cx(first === -1 || second === 1 ? 'hidden' : '')}>
				{render()}
				<button
					className={cx('next')}
					onClick={() => {
						setSecond(1)
					}}
				>
					Next
				</button>
			</div>
			{second ? <Play arr={arr} first={first} /> : <></>}
		</div>
	)
}
