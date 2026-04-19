import { useState, useEffect } from "react"
import { api } from "../api"

export default function Dashboard({ token, onLogout }) {
  const [tasks, setTasks] = useState([])
  const [title, setTitle] = useState("")
  const [description, setDescription] = useState("")
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadTasks()
  }, [])

  const loadTasks = async () => {
    const data = await api.getTasks(token)
    setTasks(Array.isArray(data) ? data : [])
    setLoading(false)
  }

  const handleAdd = async () => {
    if (!title.trim()) return
    await api.createTask(token, title, description)
    setTitle("")
    setDescription("")
    loadTasks()
  }

  const handleDelete = async (id) => {
    await api.deleteTask(token, id)
    loadTasks()
  }

  const handleToggle = async (task) => {
    await api.updateTask(token, task.id, { done: !task.done })
    loadTasks()
  }

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-2xl mx-auto">

        {/* Header */}
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-bold text-blue-600">My Tasks</h1>
          <button
            onClick={onLogout}
            className="text-sm text-gray-500 hover:text-red-500 transition"
          >
            Logout
          </button>
        </div>

        {/* Add Task Form */}
        <div className="bg-white p-4 rounded-2xl shadow mb-6">
          <h2 className="font-semibold text-gray-700 mb-3">Add New Task</h2>
          <input
            type="text"
            placeholder="Task title"
            value={title}
            onChange={e => setTitle(e.target.value)}
            className="w-full border border-gray-300 rounded-lg px-4 py-2 mb-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
          <input
            type="text"
            placeholder="Description (optional)"
            value={description}
            onChange={e => setDescription(e.target.value)}
            className="w-full border border-gray-300 rounded-lg px-4 py-2 mb-3 focus:outline-none focus:ring-2 focus:ring-blue-400"
          />
          <button
            onClick={handleAdd}
            className="w-full bg-blue-600 text-white py-2 rounded-lg font-semibold hover:bg-blue-700 transition"
          >
            + Add Task
          </button>
        </div>

        {/* Task List */}
        <div className="space-y-3">
          {loading && <p className="text-center text-gray-400">Loading tasks...</p>}
          {!loading && tasks.length === 0 && (
            <p className="text-center text-gray-400">No tasks yet. Add one above!</p>
          )}
          {tasks.map(task => (
            <div
              key={task.id}
              className="bg-white p-4 rounded-2xl shadow flex items-start justify-between gap-3"
            >
              <div className="flex items-start gap-3">
                <input
                  type="checkbox"
                  checked={task.done}
                  onChange={() => handleToggle(task)}
                  className="mt-1 cursor-pointer w-4 h-4 accent-blue-600"
                />
                <div>
                  <p className={`font-medium ${task.done ? "line-through text-gray-400" : "text-gray-800"}`}>
                    {task.title}
                  </p>
                  {task.description && (
                    <p className="text-sm text-gray-500">{task.description}</p>
                  )}
                </div>
              </div>
              <button
                onClick={() => handleDelete(task.id)}
                className="text-red-400 hover:text-red-600 text-sm transition"
              >
                Delete
              </button>
            </div>
          ))}
        </div>

      </div>
    </div>
  )
}