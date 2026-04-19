import { useState, useEffect } from "react"
import { api } from "../api"

export default function Dashboard({ token, onLogout }) {
  const [tasks, setTasks] = useState([])
  const [title, setTitle] = useState("")
  const [description, setDescription] = useState("")
  const [loading, setLoading] = useState(true)
  const [filter, setFilter] = useState("all")

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

  const filteredTasks = tasks.filter(task => {
    if (filter === "pending") return !task.done
    if (filter === "done") return task.done
    return true
  })

  const doneCount = tasks.filter(t => t.done).length
  const pendingCount = tasks.filter(t => !t.done).length

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="max-w-2xl mx-auto">

        {/* Header */}
        <div className="flex justify-between items-center mb-6">
          <div>
            <h1 className="text-2xl font-bold text-blue-600">My Tasks</h1>
            <p className="text-sm text-gray-500">{pendingCount} pending · {doneCount} completed</p>
          </div>
          <button
            onClick={onLogout}
            className="text-sm bg-white border border-gray-200 text-gray-600 px-4 py-2 rounded-lg hover:text-red-500 hover:border-red-300 transition"
          >
            Logout
          </button>
        </div>

        {/* Add Task */}
        <div className="bg-white p-5 rounded-2xl shadow mb-5">
          <h2 className="font-semibold text-gray-700 mb-3">Add New Task</h2>
          <input
            type="text"
            placeholder="Task title *"
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

        {/* Filter Tabs */}
        <div className="flex gap-2 mb-4">
          {["all", "pending", "done"].map(f => (
            <button
              key={f}
              onClick={() => setFilter(f)}
              className={`px-4 py-1.5 rounded-full text-sm font-medium transition capitalize ${
                filter === f
                  ? "bg-blue-600 text-white"
                  : "bg-white text-gray-500 hover:bg-blue-50"
              }`}
            >
              {f}
            </button>
          ))}
        </div>

        {/* Task List */}
        <div className="space-y-3">
          {loading && <p className="text-center text-gray-400 py-8">Loading tasks...</p>}
          {!loading && filteredTasks.length === 0 && (
            <div className="text-center text-gray-400 py-8 bg-white rounded-2xl">
              No tasks here. Add one above!
            </div>
          )}
          {filteredTasks.map(task => (
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
                    <p className="text-sm text-gray-500 mt-0.5">{task.description}</p>
                  )}
                </div>
              </div>
              <button
                onClick={() => handleDelete(task.id)}
                className="text-red-400 hover:text-red-600 text-sm transition shrink-0"
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