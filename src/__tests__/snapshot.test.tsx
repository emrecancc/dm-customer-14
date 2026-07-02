import React from 'react';
import { render } from '@testing-library/react';
import Dashboard from '../Dashboard';

// Mock the current date to ensure snapshot stability
jest.spyOn(Date, 'now').mockReturnValue(new Date('2024-01-14').getTime());

test('Dashboard renders correctly', () => {
  const { container } = render(<Dashboard />);
  expect(container).toMatchSnapshot();
});