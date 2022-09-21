import React, { useState, useEffect } from 'react'
import styles from './play.module.scss'
import classnames from 'classnames/bind'
const cx = classnames.bind(styles)

export default function Play({ arr, first }) {
	const [board, setBoard] = useState(arr)
	useEffect(() => {
		const body = {
			arr: arr,
			first: first,
		}
		fetch('http://localhost:8000/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(body),
		})
			.then(res => res.json())
			.then(res => {
				setBoard(
					res.map(i => {
						return i
					})
				)
			})
			.catch(err => {
				console.log('error')
			})
    if(first===0){
      const body = { arr: board, x: -1, y: -1 }
      fetch('http://localhost:8000/play', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify(body),
			})
				.then(res => res.json())
				.then(res => {
					setBoard(
						res.map(i => {
							return i
						})
					)
				})
				.catch(err => {
					console.log('error')
				})
    }
	}, [])
	const render = () => {
		const ret = []
		for (let i = 0; i < 8; i++) {
			ret.push(
				<div key={i} className={cx('row')}>
					{board[i].map((j, ix) => {
						return (
							<div
								onClick={() => {
									const body = { arr: board, x: i, y: ix }
									fetch('http://localhost:8000/play', {
										method: 'POST',
										headers: {
											'Content-Type': 'application/json',
										},
										body: JSON.stringify(body),
									})
										.then(res => res.json())
										.then(res => {
											setBoard(res.map(i => {return i}))
										})
										.catch(err => {
											console.log('error')
										})
								}}
								key={i * 8 + ix}
								className={cx('cell', j === 0 ? 'zero' : j === 1 ? 'one' : j === -1 ? 'hole' : 'two')}
							>
							</div>
						)
					})}
				</div>
			)
		}
		return ret
	}
	return <div>{render()}</div>
}
